import pygame

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

while game:
    clock.tick(fps)
    screen.fill("white")
    
    for event in pygame.event.get():
        if event.type == pygame.FINGERDOWN:
            fingers[str(event.finger_id)] = (event.x * width, event.y * height)
        if event.type == pygame.FINGERMOTION:
            fingers[str(event.finger_id)] = (event.x * width, event.y * height)
        if event.type == pygame.FINGERUP:
            del fingers[str(event.finger_id)]            
    
    for i in fingers:
        pygame.draw.circle(screen, "black", fingers[i], 100, 5)
    
    pygame.display.flip()