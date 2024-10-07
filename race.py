import pygame
from pygame.math import *
import math

from random import randint

pygame.init()

scr = (width, height) = (0, 0)
screen = pygame.display.set_mode((width, height))
screen2 = pygame.Surface((1000, 1000))
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
#init clock for fps manipulation
clock = pygame.time.Clock()
#feel free to edit the fps of your game
fps = 60
game = True

right = Vector2(1, 0)

class Car:
    pos = Vector2(0, 0)
    rotation = 0
    vel = Vector2(0, 0)
    forward = 0
    
    skid = False
    def __init__(self, base):
        self.base = pygame.transform.rotate(base, 90)
        self.surf = pygame.transform.rotate(self.base, self.rotation)
        
    def tick(self):
        angle = math.radians(-self.rotation)
        self.vel = Vector2(math.cos(angle), math.sin(angle)) * self.forward
        self.forward *= 0.9
        
        self.pos = self.pos + self.vel
        
        self.surf = pygame.transform.rotate(self.base, self.rotation)
    def move(self, rot, throttle):
        self.rotation += rot * throttle * 0.3
        self.forward += throttle
    def render(self, surface):
        pos = self.pos
        rr = self.surf.get_rect()
        pos = Vector2(width, height)*0.5 - Vector2(rr.w//2, rr.h//2)
        surface.blit(self.surf, pos)
        

class Joystick:
    def __init__(self, pos):
        self.pos = pos
        self.handle = pos
        self.output = Vector2(0, 0)
    def update(self, finger):
        x, y = finger
        pos = self.pos
        
        x -= pos[0]
        y -= pos[1]
        
        scale = math.sqrt(x**2 + y**2)
        if scale < 20:
            self.handle = pos
            self.output = Vector2(0, 0)
            return self.handle
        x = x / scale
        y = y / scale 
        
        self.output = Vector2(x, y)
        
        x = x * 100 + pos[0]
        y = y * 100 + pos[1]
        
        self.handle = (x, y)
        return self.handle
    def render(self, surface):
        pygame.draw.circle(surface, "black", self.pos, 200, 10)
        pygame.draw.circle(surface, "black", self.handle, 50)


car = Car(pygame.image.load("placeholder.png").convert_alpha())
car.pos = Vector2()

fingers = {}
joysticks = {}

trees = []
for i in range(500):
    trees.append(Vector2(randint(-5000, 5000), randint(-10000, 10000)))

while game:
    clock.tick(fps)
    
    screen.fill("white")
    
    for event in pygame.event.get():
        if event.type == pygame.FINGERDOWN:
            if len(list(joysticks)) == 0:
                fingers[str(event.finger_id)] = Vector2(event.x * width, event.y * height)
                joysticks[str(event.finger_id)] = Joystick(Vector2(event.x * width, event.y * height))
        if event.type == pygame.FINGERMOTION:
            try:
                fingers[str(event.finger_id)] = Vector2(event.x * width, event.y * height)
            except:
                pass
        if event.type == pygame.FINGERUP:
            try:
                del fingers[str(event.finger_id)]
                del joysticks[str(event.finger_id)]
            except:
                pass
    
    
    car.render(screen)
    
    for tree in trees:
        pygame.draw.circle(screen, "green3", tree-car.pos, 30)
        pygame.draw.circle(screen, "green2", tree-car.pos, 20)
        pygame.draw.circle(screen, "green", tree-car.pos, 5)
        
        
    for i in fingers:
        pygame.draw.circle(screen, "black", fingers[i], 100, 5)    
    for i in joysticks:
        joysticks[i].update(fingers[i])
        out = joysticks[i].output
        delta = - out.x * 5
        
        car.move(delta, (abs(out.y) > 0) * 2)
        
        joysticks[i].render(screen)
    car.tick()
    pygame.display.flip()
