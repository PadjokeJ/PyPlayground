import pygame
import math
import random
from physics import v2
from fps import frames
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
    pos = (0, 0)
    finger = 0
    def __init__(self):
        print("new joystick")
    def input(self, fingers):
        pos = self.pos
        if self.finger in fingers and len(fingers):
            finger = fingers[self.finger]
            input = (finger[0] - pos[0], finger[1] - pos[1])
            # normalize
            scale = input[0]**2 + input[1]**2
            scale = math.sqrt(scale)
            scale = max(0.001, scale)
            mult = 1 / scale
            input = (input[0] * mult, input[1] * mult)
            
            return input
        else:
            if len(fingers) == 0:
                return (0, 0)
            min_dist = 999
            for key in fingers:
                x, y = fingers[key]
                dx = x - pos[0]
                dy = y - pos[1]
                if math.sqrt(dx**2 + dy**2) < min_dist:
                    finger = key
                    min_dist = math.sqrt(dx**2 + dy**2)
            try:
                self.finger = finger
            except:
                self.finger = 0
            return (0, 0)
    def render(self, surface, color, size):
        pos = self.pos
        pygame.draw.circle(surface, color, pos, size, 20)
                

class Player:
    pos = (0, 0)
    vel = (0, 0)
    def __init__(self):
        print("new player")
    def move(self, tuple, speed):
        x, y = self.pos
        if x > width:
            x = 0
        if x < 0:
            x = width
        if y > height:
            y = 0
        if y < 0:
            y = height
        dx, dy = self.vel
        dx += tuple[0] * speed
        dy += tuple[1] * speed
        self.vel = (dx * 0.99, dy * 0.99)
        self.pos = (x + dx, y + dy)
    def render(self, surface):
        pygame.draw.circle(surface, "red2", self.pos, 20)

def random_pos():
    return v2(random.randint(0, 1) * width, random.randint(0, 1) * height)

class Asteroid:
    def __init__(self, dir, speed):
        self.dir = dir.scale(speed)
        self.speed = speed
        self.size = random.randint(50, 100)
        self.pos = random_pos()
    def move(self):
        self.pos.add(self.dir)
        if self.pos.x > width + self.size:
            self.pos.x = 0
        if self.pos.x < -self.size:
            self.pos.x = width
        if self.pos.y > height + self.size:
            self.pos.y = 0
        if self.pos.y < -self.size:
            self.pos.y = height
    def render1(self, surface):
        pygame.draw.circle(surface, "gray30", self.pos.tuple(), self.size)
    def render2(self, surface):
        pygame.draw.circle(surface, "gray20", self.pos.tuple(), self.size - 20)



fingers = {}

move = Joystick()
move.pos = (width // 2, height - 200)
player = Player()
player.pos = (width//2, height//2)

particles = []
asteroids = []
ticker = 0
max_tick = 80

score = 0
score_font = pygame.font.SysFont(None, 60)

max_fuel = 600
fuel = max_fuel

while game:
    clock.tick(fps)
    screen.fill("black")
    
    for event in pygame.event.get():
        if event.type == pygame.FINGERDOWN:
            fingers[str(event.finger_id)] = (event.x * width, event.y * height)
        if event.type == pygame.FINGERMOTION:
            fingers[str(event.finger_id)] = (event.x * width, event.y * height)
        if event.type == pygame.FINGERUP:
            del fingers[str(event.finger_id)]
        if event.type == pygame.QUIT:
            game = False
            exit()
    
    inp = move.input(fingers)
        
    if inp[0] + inp[1] != 0:
        x, y = inp
        rand = (random.randint(0, 10) / 10 - 0.5, random.randint(0, 10) / 10 - 0.5)
        particles.append([player.pos, (-x * 5 + rand[0] + player.vel[0] * 1, -y * 5 + rand[1] + player.vel[1] * 1), 10 + random.randint(0, 100) / 10 - 0.5])
    iter = len(particles) - 1
    
    
    
    for i in reversed(particles):
        i[0] = (i[1][0] + i[0][0], i[1][1] + i[0][1])
        i[2] -= 0.2
        pygame.draw.circle(screen, "white", i[0], int(i[2]))
        if i[2] < 0:
            particles.pop(iter)
        iter -= 1
    for i in reversed(particles):
        pygame.draw.circle(screen, "gray", i[0], int(i[2])-4)
    
    ticker += 1
    
    if ticker > max_tick:
        max_tick -= 1
        ticker = 0
        score += 1
        asteroids.append(Asteroid(v2(random.randint(-100, 100), random.randint(-100, 100)).normalize(), random.randint(1, 7)))
    
    playerpos = v2().from_tuple(player.pos)
    for ast in asteroids:
        ast.move()
        if ast.pos.distance(playerpos) < ast.size + 20:
            game = False
        ast.render1(screen)
    
    for ast in asteroids:
        ast.render2(screen)
    
    
    player.move(inp, 0.2)
    
    player.render(screen)
    
    
    #-----# UI #-----#
    
    move.render(screen, "white", 150)
    
    frames(screen, clock, "white")
    _score = score_font.render(str(score), 1, "white")
    score_pos = _score.get_rect().center
    screen.blit(_score, (width//2 - score_pos[0], 0))
    
    for i in fingers:
        pygame.draw.circle(screen, "white", fingers[i], 100, 5)
        
    pygame.display.flip()
i = 0
particles.clear()
_particles = []
ticker = 0
max_tick = 5
death = False
spaceship = True
while not death:
    screen.fill("black")
    clock.tick(60)
    ticker += 1
    if ticker > max_tick:
        ticker = 0
        try:
            pos = v2().copy(asteroids[0].pos)
            print(pos)
            _particles.append([v2().from_tuple(player.pos), v2(random.randint(-100, 100), random.randint(-100, 100)).normalize().scale(random.randint(1, 60) / 10), random.randint(50, 250)/10, 0.5])
            for i in range(60):
                particles.append([v2().copy(pos), v2(random.randint(-100, 100), random.randint(-100, 100)).normalize().scale(random.randint(10, 200) / 10), random.randint(250, 500)/10, 1])
            asteroids.pop(0)
        except:
            if spaceship:
                spaceship = False
                max_tick = 60
                for i in range(60):
                    _particles.append([v2().from_tuple(player.pos), v2(random.randint(-100, 100), random.randint(-100, 100)).normalize().scale(random.randint(1, 60) / 10), random.randint(100, 250)/10, 0.5])
            if len(particles) == 0:
                death = True
    
    for ast in asteroids:
        ast.render1(screen)
    for ast in asteroids:
        ast.render2(screen)
    
    for part in reversed(particles):
        part[0].add(part[1])
        part[1].scale(0.95)
        part[2] -= part[3]
        pygame.draw.circle(screen, "gray20", part[0].tuple(), int(part[2]))
        if part[2] < 0:
            particles.remove(part)
    for part in particles:
        pygame.draw.circle(screen, "gray30", part[0].tuple(), int(part[2]) - 5)
    
    for part in reversed(_particles):
        part[0].add(part[1])
        part[1].scale(0.95)
        part[2] -= part[3]
        pygame.draw.circle(screen, "red4", part[0].tuple(), int(part[2]))
        if part[2] < 0:
            _particles.remove(part)
    for part in _particles:
        pygame.draw.circle(screen, "red", part[0].tuple(), int(part[2]) - 5)
        
    
    if spaceship:
        player.render(screen)
    screen.blit(_score, (width//2 - score_pos[0], 0))
    frames(screen, clock, "white")
    pygame.display.flip()