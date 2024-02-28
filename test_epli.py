import cv2
import numpy as np
import matplotlib.pyplot as plt

# 원 이미지 생성 (원이 타원으로 보이도록)
img_size = (500, 500)
image = np.zeros((img_size[0], img_size[1], 3), dtype=np.uint8)

# 중심 좌표와 반지름 설정
center = (img_size[1] // 2, img_size[0] // 2)
radius = 200

# 원 그리기
cv2.circle(image, center, radius, (255, 255, 255), -1)

# 렌즈 왜곡 모델링을 위해 카메라 매트릭스 설정
focal_length = 300
camera_matrix = np.array([[focal_length, 0, img_size[1] // 2],[0, focal_length, img_size[0] // 2],[0, 0, 1]], dtype=np.float32)

# 렌즈 왜곡 계수 설정
dist_coeffs = np.array([0.8, 0.4, 0.5, 0.3], dtype=np.float32)

# 렌즈 왜곡 보정
distorted_image = cv2.undistort(image, camera_matrix, dist_coeffs)

# 시각화
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(distorted_image)
plt.title('Distorted Image (Lens Distortion)')
plt.show()
