import pygame
import math

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

class Joystick:
    def __init__(self, pos):
        self.pos = pos
        self.handle = pos
        self.output = (0, 0)
    def update(self, finger):
        x, y = finger
        pos = self.pos
        
        x -= pos[0]
        y -= pos[1]
        
        scale = math.sqrt(x**2 + y**2)
        if scale < 20:
            self.handle = pos
            return self.handle
        x = x / scale
        y = y / scale 
        
        self.output = (x, y)
        
        x = x * 100 + pos[0]
        y = y * 100 + pos[1]
        
        self.handle = (x, y)
        return self.handle
    def render(self, surface):
        pygame.draw.circle(surface, "black", self.pos, 200, 10)
        pygame.draw.circle(surface, "black", self.handle, 50)


fingers = {}
joysticks = {}

while game:
    clock.tick(fps)
    screen.fill("white")
    
    for event in pygame.event.get():
        if event.type == pygame.FINGERDOWN:
            if event.finger_id < 2:
                fingers[str(event.finger_id)] = (event.x * width, event.y * height)
                joysticks[str(event.finger_id)] = Joystick((event.x * width, event.y * height))
        if event.type == pygame.FINGERMOTION:
            try:
                fingers[str(event.finger_id)] = (event.x * width, event.y * height)
            except:
                pass
        if event.type == pygame.FINGERUP:
            try:
                del fingers[str(event.finger_id)]
                del joysticks[str(event.finger_id)]
            except:
                pass
    
    for i in fingers:
        pygame.draw.circle(screen, "black", fingers[i], 100, 5)    
    for i in joysticks:
        joysticks[i].update(fingers[i])
        joysticks[i].render(screen)
    pygame.display.flip()