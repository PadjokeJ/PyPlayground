import pygame
import math
scr = (width, height) = (0, 0)
screen = pygame.display.set_mode((width, height))
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
#init clock for fps manipulation
clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.SysFont(None, 30)

#feel free to edit the fps of your game
fps = 60
game = True

half_h = height // 2
pi = 3.142
deg2rad = 2 * pi / width

lerp = 0

freq = 1
_f = freq
h = half_h
_h = h

r = pygame.Rect((0, 0), (400, 100))

def func(x):
    val = x * deg2rad * _f
    y = math.sin(val) * h 
    if abs(y) < 5:
        pygame.draw.circle(screen, "green", (x, half_h), 4)
    return y

n = 5


while game:
    clock.tick()
    
    freq = int(pygame.mouse.get_pos()[0] ** 2 / width ** 1.5)
    h = pygame.mouse.get_pos()[1] / 2
    lerp += 0.02
    if (freq != _f):
        _f = (freq + _f * 9) / 10
        screen.fill("black")
        _y = half_h
        pygame.draw.line(screen, "red", (0, half_h), (width, half_h), 2)
        for i in range(width * n):
            y = half_h - func(i / n)
            pygame.draw.line(screen, "blue", (i / n, y), ((i - 1) / n, _y), 5)
            _y = y
    else:
        _f = int(freq)
    if (abs(freq - _f) < 0.001):
        _f = freq
        
        
    pygame.draw.rect(screen, "black", r)
    fps = int(clock.get_fps())
    _fps = font.render(str(fps) + "fps", 1, "white")
    screen.blit(_fps, (20, 0))
    
    t_freq = font.render(f"freq : {freq} : {round(_f, 3)}", 1, "white")
    screen.blit(t_freq, (20, 40))
    
    pygame.display.flip()