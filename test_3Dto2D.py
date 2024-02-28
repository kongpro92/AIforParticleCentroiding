from Camera import *
import pandas as pd

# 예제 사용법
if __name__ == "__main__":
    # 예제 내부 파라미터, 외부 파라미터, 왜곡 파라미터
    fx, fy, cx, cy = 16000, 16000, 256, 256
    k1, k2, p1, p2, k3 = 0,0,0,0,0
    rx, ry, rz = 0.0, 0.0, 0.0 # 라디안
    tx, ty, tz = 0.0, 0.0, 1000.0 # 미터

    # 내부 파라미터 및 외부 파라미터 설정
    camera_matrix = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]], dtype=np.float32)
    distortion_coefficients = np.array([k1, k2, p1, p2, k3], dtype=np.float32)
    rotation_vector = np.array([rx, ry, rz], dtype=np.float32)
    translation_vector = np.array([tx, ty, tz], dtype=np.float32)

    # CustomCamera 객체 생성 및 파라미터 설정
    custom_camera = Camera(camera_matrix, distortion_coefficients, rotation_vector, translation_vector)
    
    par_num = 10
    particle_diameter = 0.1
    boundary = Boundary(-10,-10,-10,10,10,10)
    particles_system = Particles3D(par_num, particle_diameter)
    particles_system.GenerateParticle(boundary)
    #particles_system.particles_pos.append([0,0.01,0])
    
    
    # 3D 입자 좌표 설정 (예: X, Y, Z 좌표)
    particle_3d = np.array([particles_system.particles_pos], dtype=np.float32)

    # 3D 좌표를 2D 이미지 좌표로 변환
    particle_2d = custom_camera.project_3d_to_2d(particle_3d)

    # 변환된 이미지 좌표 출력
    print("3D Particle Coordinates:", particle_3d)
    print("2D Image Coordinates:", particle_2d)
    
    # 640x320 사이즈의 이미지 생성
    image_size = (512, 512)
    image = np.zeros((image_size[1], image_size[0]), dtype=np.float32)
    
    def gaussian(x, y, cx, cy, sigma):
        return np.exp(-((x - cx)**2 + (y - cy)**2) / (2 * sigma**2))

    def draw_gaussian(image, center, sigma,par_size):
        parsize = par_size -1
        h, w = image.shape[:2]
        for cent in center:
            center_x, center_y = int(cent[0]),int(cent[1])
            for y in range(center_y - parsize, center_y + parsize+1):
                for x in range(center_x - parsize, center_x + parsize+1):
                    if 0 <= x < w and 0 <= y < h:
                        intensity = gaussian(x, y, cent[0], cent[1], sigma)
                        image[y, x] += (intensity *255)
        for y in range(h):
            for x in range(w):
                if image[y, x] >= 255:
                    image[y, x] = 255
                

    def peakFinder(image,thr):
        cnt = 0
        h, w = image.shape[:2]
        for y in range(1,h):
            for x in range(1,w):
                #print(type(image[y-1:y+2, x-1:x+2]),image[y,x])
                if np.max(image[y-1:y+2, x-1:x+2]) == image[y,x] and image[y,x] >thr:
                    cnt +=1
        print(cnt)

    point = particle_2d.astype(np.float32)
    draw_gaussian(image, point, sigma=5,par_size=5)
    
    #df = pd.DataFrame(image)
    #print(df)
    
    peakFinder(image,35)
    
    uint8_image = np.round(image).astype(np.uint8)
    
    
    res_show = cv2.applyColorMap(uint8_image, cv2.COLORMAP_PARULA)

    # 결과 이미지 출력
    cv2.imshow("Points on Image", res_show)
    cv2.waitKey(0)
    cv2.destroyAllWindows()