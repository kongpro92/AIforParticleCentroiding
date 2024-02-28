import random
import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from tqdm import tqdm
from Boundary import Boundary

class Particle3D:
    def __init__(self, x, y, z):
        self.pos = np.array([x,y,z])

class Particles3D:
    def __init__(self, par_num, particle_diameter):
        self.par_num = par_num
        self.particles_pos = []
        self.diameter = particle_diameter

    def GenerateParticle(self,boundary:Boundary):
        with tqdm(total=self.par_num, desc="Generating Particles", unit="particles") as pbar:
            while len(self.particles_pos) < self.par_num:
                x = random.uniform(boundary.Min_X, boundary.Max_X)
                y = random.uniform(boundary.Min_Y, boundary.Max_Y)
                z = random.uniform(boundary.Min_Z, boundary.Max_Z)
                
                new_particle = Particle3D(x, y, z)

                if not any(self.IsOverlapParticlePostion(existing_particle, new_particle.pos) for existing_particle in self.particles_pos):
                    self.particles_pos.append(new_particle.pos)
                    pbar.update(1)

    def IsOverlapParticlePostion(self,par1:Particle3D,par2:Particle3D):
        distance = np.linalg.norm(par1-par2)
        return distance < self.diameter

    def visualize(self, b:Boundary):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        boundaries = [
        [(b.Min_X, b.Max_X), (b.Min_Y, b.Min_Y), (b.Min_Z, b.Min_Z)],
        [(b.Min_X, b.Max_X), (b.Min_Y, b.Min_Y), (b.Max_Z, b.Max_Z)],
        [(b.Min_X, b.Min_X), (b.Min_Y, b.Max_Y), (b.Min_Z, b.Min_Z)],
        [(b.Max_X, b.Max_X), (b.Min_Y, b.Max_Y), (b.Max_Z, b.Max_Z)],
        [(b.Min_X, b.Min_X), (b.Min_Y, b.Min_Y), (b.Min_Z, b.Max_Z)],
        [(b.Min_X, b.Min_X), (b.Max_Y, b.Max_Y), (b.Min_Z, b.Max_Z)],
        [(b.Min_X, b.Min_X), (b.Min_Y, b.Max_Y), (b.Max_Z, b.Max_Z)],
        [(b.Max_X, b.Max_X), (b.Min_Y, b.Max_Y), (b.Min_Z, b.Min_Z)],
        [(b.Min_X, b.Max_X), (b.Max_Y, b.Max_Y), (b.Min_Z, b.Min_Z)],
        [(b.Min_X, b.Max_X), (b.Max_Y, b.Max_Y), (b.Max_Z, b.Max_Z)],
        [(b.Max_X, b.Max_X), (b.Min_Y, b.Min_Y), (b.Min_Z, b.Max_Z)],
        [(b.Max_X, b.Max_X), (b.Max_Y, b.Max_Y), (b.Min_Z, b.Max_Z)],
        ]

        for b in boundaries:
            ax.plot(b[0], b[1], b[2], color='b',  alpha=.15,linewidth=2)

        # 입자를 표시
        for particle in self.particles_pos:
            par = particle.tolist()
            ax.scatter(par[0],par[1],par[2], s=(self.diameter**2)*100, color='r',marker='o')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.show()
    
if __name__ == "__main__":
    par_num = 1000
    particle_diameter = 0.1
    boundary = Boundary(-10,-10,-10,10,10,10)
    particles_system = Particles3D(par_num, particle_diameter)
    particles_system.GenerateParticle(boundary)
    particles_system.visualize(boundary)