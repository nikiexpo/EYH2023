import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 800, 800
BLUE = (0,0,255)
GREY = (125, 125, 125)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Debris Removal")

class SpaceObject:
    G = 6.67428e-11
    Km = 1000 #meters
    scale = 800/(2*900*Km)    # 800 pixels = 900Km
    delta = 1 # time step = 4 hours

    def __init__(self, x, y, radius, mass, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.color = color

        self.orbit = []
        self.isEarth = False
        self.distanceToEarth = 0
        self.isSatellite = False

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.scale + WIDTH/2
        y = self.y * self.scale + HEIGHT/2
        pygame.draw.circle(win, self.color, (x,y), self.radius)
        if self.isSatellite:
            #pygame.draw.line(win, RED, (x, y), (WIDTH/2,HEIGHT/2), 5)
            pass
    
    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.isEarth:
            self.distanceToEarth = distance
        
        force = (self.G * self.mass * other.mass)/(distance**2)
        #print(force)
        #print(resultant)
        theta = math.atan2(distance_y, distance_x)
        force_x = force * math.cos(theta)
        force_y = force * math.sin(theta)
        #print(force_x, " - ", force_y)
        return force_x, force_y
    
    def updatePosition(self, planet):

        if self == planet:
            return
        fx, fy = self.attraction(planet)
        self.x_vel += (fx / self.mass) * self.delta
        self.y_vel += (fy / self.mass) * self.delta

        self.x += self.x_vel * self.delta
        self.y += self.y_vel * self.delta
        self.orbit.append((self.x, self.y))

    def drawLaser(self, x1, y1, x2, y2, win):
        pass

    def laser(self, sat, win):
        x = self.x * self.scale + WIDTH/2
        y = self.y * self.scale + HEIGHT/2
        x1 = sat.x * self.scale + WIDTH/2
        y1 = sat.y * self.scale + HEIGHT/2

        if self.isEarth:
            return
        if self.isSatellite:
            return
        if abs(self.x - sat.x) < 2000:
            pygame.draw.line(win, RED, (x, y), (x1, y1), 5)
            print("hit")
    
    
        

def debriGenerator(list, distances):
    for dis in distances:
        deb = SpaceObject(-1*dis*1000, 0, 1, 0.1, WHITE)
        deb.y_vel = 20*1000
        list.append(deb)

def randomDistanceGen(num, distances):
    while num > 0:
        num = num -1
        distances.append(random.randint(440, 600))


def main():
    run = True
    clock = pygame.time.Clock()
    
    distances = []
    randomDistanceGen(10, distances)

    earth = SpaceObject(0,0, 30, 5.9722 * 10**24, BLUE)
    earth.isEarth = True
        
    satellite = SpaceObject(-800*1000, 0, 8, 1000,GREY ) # radius scaled up by 3*10^5
    satellite.isSatellite = True
    satellite.y_vel = 20.5*1000

    debri_1 = SpaceObject(-500*1000, 0, 2, 0.1 , WHITE) # radius scaled up by 12*10^6 
    debri_1.y_vel = 30*1000

    objects = [earth, satellite, debri_1]

    debriGenerator(objects, distances)

    while run:

        clock.tick(14)
        WIN.fill((0,0,0))
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        for obj in objects:
            obj.updatePosition(earth)
            #print(obj.x, obj.y)
            obj.laser(satellite, WIN)
            obj.draw(WIN)
        
        pygame.display.update()

    pygame.quit()

main()