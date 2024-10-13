import pygame
import math
scr = (width, height) = (0, 0)
screen = pygame.display.set_mode((width, height))
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
#init clock for fps manipulation
clock = pygame.time.Clock()
#feel free to edit the fps of your game
fps = 60
game = True

half_h = height // 2
pi = 3.142
deg2rad = 2 * pi / width

lerp = 0

freq = 1
h = half_h

def func(x):
    val = x * deg2rad * freq
    y = math.cos(val) * h
    if abs(y) < 1:
        pygame.draw.circle(screen, "green", (x, half_h - y), 20)
    return y

while game:
    clock.tick()
    screen.fill("black")
    freq = pygame.mouse.get_pos()[0] / 50
    h = pygame.mouse.get_pos()[1] / 2
    lerp += 0.02
    pygame.draw.line(screen, "red", (0, half_h), (width, half_h), 2)
    for i in range(width * 10):
        pygame.draw.circle(screen, "blue", (i/10, half_h - func(i/10)), 1)
    pygame.display.flip()