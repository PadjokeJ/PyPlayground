import pygame

pygame.font.init()
font = pygame.font.SysFont(None, 30)

def frames(surface, clock, color):
    fps = int(clock.get_fps())
    _fps = font.render(str(fps) + "fps", 1, color)
    surface.blit(_fps, (20, 0))
def render(surface, str):
    _str = font.render(str, 1, "black")
    surface.blit(_str, (0, 20))
def render_mult(surface, str):
    for i in range(len(str)):
        _str = font.render(str[i], 1, "black")
        surface.blit(_str, (0, 20 * (i + 1)))