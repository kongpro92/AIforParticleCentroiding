import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class Boundary():
    def __init__(self,min_x,min_y,min_z,max_x,max_y,max_z) -> None:
        self.Min_X = min_x
        self.Min_Y = min_y
        self.Min_Z = min_z
        self.Max_X = max_x
        self.Max_Y = max_y
        self.Max_Z = max_z
        
    def ShowBoundary(self):
        vertices = [
                    (self.Min_X, self.Min_Y, self.Min_Z),
                    (self.Min_X, self.Min_Y, self.Max_Z),
                    (self.Min_X, self.Max_Y, self.Min_Z),
                    (self.Min_X, self.Max_Y, self.Max_Z),
                    (self.Max_X, self.Min_Y, self.Min_Z),
                    (self.Max_X, self.Min_Y, self.Max_Z),
                    (self.Max_X, self.Max_Y, self.Min_Z),
                    (self.Max_X, self.Max_Y, self.Max_Z)
                ]

                # 육면체를 이루는 면의 정점 순서
        faces = [
                    [0, 1, 3, 2],
                    [4, 5, 7, 6],
                    [0, 1, 5, 4],
                    [2, 3, 7, 6],
                    [0, 2, 6, 4],
                    [1, 3, 7, 5]
                ]

                # 육면체를 그리기 위한 Poly3DCollection 객체 생성
        Face = [[vertices[face[0]], vertices[face[1]], vertices[face[2]], vertices[face[3]]] for face in faces]
        cube = Poly3DCollection( Face,alpha=.25, edgecolor='k')


        # 그림 생성 및 설정
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # 축 범위 설정
        ax.set_xlim([self.Min_X, self.Max_X])
        ax.set_ylim([self.Min_Y, self.Max_Y])
        ax.set_zlim([self.Min_Z, self.Max_Z])

        # 육면체 추가
        ax.add_collection3d(cube)

        # 그리기
        plt.show()
        
if __name__ == "__main__":
    b = Boundary(-10,-20,-30,10,20,30)
    b.ShowBoundary()