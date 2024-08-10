import pygame
from physics import *
from random import randint as rand
from fps import frames, render

pygame.init()

scr = (width, height) = (0, 0)
screen = pygame.display.set_mode((width, height))
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
#init clock for fps manipulation
clock = pygame.time.Clock()
#feel free to edit the fps of your game
fps = 60
game = True

fingers = {}
dfingers = {}
particles = []

while game:
    clock.tick(fps)
    screen.fill("white")
    
    for event in pygame.event.get():
        if event.type == pygame.FINGERDOWN:
            fingers[str(event.finger_id)] = v2(event.x * width, event.y * height)
            dfingers[str(event.finger_id)] = v2(event.dx * width, event.dy * height)
        if event.type == pygame.FINGERMOTION:
            fingers[str(event.finger_id)] = v2(event.x * width, event.y * height)
            dfingers[str(event.finger_id)] = v2(event.dx * width * 0.5, event.dy * height * 0.5)
        if event.type == pygame.FINGERUP:
            del fingers[str(event.finger_id)]            
    
    for i in fingers:
        pygame.draw.circle(screen, "black", fingers[i].tuple(), 100, 1)
        particles.append([v2().copy(fingers[i]), v2().copy(dfingers[i]), rand(50, 100)]) # v2().copy(dfingers[i]).add(v2(rand(0, 20) / 10 - 1, -10))
    for i in reversed(particles):
        i[0].add(i[1])
        i[1].scale(0.9)
        i[2] -= 0.5
        
        pygame.draw.circle(screen, "black", i[0].tuple(), int(i[2]))
        
        if i[2] < 1:
            particles.remove(i)
    for i in reversed(particles):
        pygame.draw.circle(screen, "white", v2().copy(i[0]).tuple(), int(i[2]) - 5)
    
    render(screen, str(len(particles)))
    frames(screen, clock, "black")
    pygame.display.flip()