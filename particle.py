import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tqdm import tqdm
from Boundary import Boundary

class Particle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Particles:
    def __init__(self, par_num, particle_diameter):
        self.par_num = par_num
        self.particles = []
        self.diameter = particle_diameter

    def GenerateParticle(self,boundary:Boundary):
        with tqdm(total=self.par_num, desc="Generating Particles", unit="particles") as pbar:
            while len(self.particles) < self.par_num:
                x = random.uniform(boundary.Min_X, boundary.Max_X)
                y = random.uniform(boundary.Min_Y, boundary.Max_Y)
                z = random.uniform(boundary.Min_Z, boundary.Max_Z)
                
                new_particle = Particle(x, y, z)

                if not any(self.IsOverlapParticlePostion(existing_particle, new_particle) for existing_particle in self.particles):
                    self.particles.append(new_particle)
                    pbar.update(1)

    def IsOverlapParticlePostion(self,par1:Particle,par2:Particle):
        distance = math.sqrt((par1.x - par2.x)**2 + (par1.y - par2.y)**2 + (par1.z - par2.z)**2)
        return distance < self.diameter

    def visualize(self, boundary):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        boundaries = [
        [(boundary.Min_X, boundary.Max_X), (boundary.Min_Y, boundary.Min_Y), (boundary.Min_Z, boundary.Min_Z)],
        [(boundary.Min_X, boundary.Max_X), (boundary.Min_Y, boundary.Min_Y), (boundary.Max_Z, boundary.Max_Z)],
        [(boundary.Min_X, boundary.Min_X), (boundary.Min_Y, boundary.Max_Y), (boundary.Min_Z, boundary.Min_Z)],
        [(boundary.Max_X, boundary.Max_X), (boundary.Min_Y, boundary.Max_Y), (boundary.Max_Z, boundary.Max_Z)],
        [(boundary.Min_X, boundary.Min_X), (boundary.Min_Y, boundary.Min_Y), (boundary.Min_Z, boundary.Max_Z)],
        [(boundary.Min_X, boundary.Min_X), (boundary.Max_Y, boundary.Max_Y), (boundary.Min_Z, boundary.Max_Z)],
        [(boundary.Min_X, boundary.Min_X), (boundary.Min_Y, boundary.Max_Y), (boundary.Max_Z, boundary.Max_Z)],
        [(boundary.Max_X, boundary.Max_X), (boundary.Min_Y, boundary.Max_Y), (boundary.Min_Z, boundary.Min_Z)],
        [(boundary.Min_X, boundary.Max_X), (boundary.Max_Y, boundary.Max_Y), (boundary.Min_Z, boundary.Min_Z)],
        [(boundary.Min_X, boundary.Max_X), (boundary.Max_Y, boundary.Max_Y), (boundary.Max_Z, boundary.Max_Z)],
        [(boundary.Max_X, boundary.Max_X), (boundary.Min_Y, boundary.Min_Y), (boundary.Min_Z, boundary.Max_Z)],
        [(boundary.Max_X, boundary.Max_X), (boundary.Max_Y, boundary.Max_Y), (boundary.Min_Z, boundary.Max_Z)],
    ]

        for b in boundaries:
            ax.plot(b[0], b[1], b[2], color='b',  alpha=.15,linewidth=2)

        # 입자를 표시
        for particle in self.particles:
            #ax.scatter(particle.x, particle.y, particle.z, color='r', marker='o')
            ax.scatter(particle.x, particle.y, particle.z, s=(self.diameter**2)*100, color='r',marker='o')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.show()
    

# Particles 클래스의 인스턴스를 생성하고 파티클 수와 파티클 지름을 전달합니다.
par_num = 100
particle_diameter = 0.1
boundary = Boundary(-10,-10,-10,10,10,10)
particles_system = Particles(par_num, particle_diameter)
particles_system.GenerateParticle(boundary)

particles_system.visualize(boundary)