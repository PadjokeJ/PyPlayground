# IMPORTS
from random import randint as ri
from random import random as rf
import pygame

# CONSTANTS

N_BOMBS = 5
C_BOMBS = (18, 18, 25)
FLAGS_C = (250, 100, 150)

PROXIM = [(-1, 1), (0, 1), (1, 1),
                     (-1, 0),            (1, 0),
                     (-1, -1), (0, -1), (1, -1)]

pygame.init()

# VARS/VARIABLES

scr = (width, height) = (0, 0)
screen = pygame.display.set_mode((width, height))
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
#init clock for fps manipulation
clock = pygame.time.Clock()
#feel free to edit the fps of your game
fps = 60
game = True
win = False

col = [0 for i in range(20)]
board = [col.copy() for i in range(10)]
uncovered = []
flags = []

flags_bg_width = width - 200
flags_bg_height = height - 75
flags_bg_start = 100
flags_bg_end = flags_bg_start + flags_bg_width

prev = False
flags_ratio = 0

# DEFS/DEFINITIONS

def get_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

def populate(board, n):
    bombs = []
    while len(bombs) != N_BOMBS:
        x, y = ri(0, 9), ri(0, 19)
        if board[x][y] != -1:
            board[x][y] = -1
            bombs.append((x, y))
    return board, bombs

def uncover_neighbors(board, uncovered, pos):
    to_check = []
    to_check.append(pos)
    uncovered.append(pos)
    while len(to_check) > 0:
        print(f"Trying to expand to {to_check[0]}")
        for i in PROXIM:
            x = i[0] + to_check[0][0]
            y = i[1] + to_check[0][1]
            if (x >= 0) and (y >= 0):
                try:
                    if board[x][y] == 0 and not((x, y) in uncovered):
                        uncovered.append((x, y))
                        to_check.append((x, y))
                    elif board[x][y] != -1:
                        uncovered.append((x, y))
                except:
                    pass
        to_check.pop(0)
    return uncovered
            
def fcolor(board, col, p):
    return (255 - 10* board[col][p], max(40, int(255 - 15* board[col][p] ** 2)), max(40, int(255 - 15* board[col][p] ** 2)))

def render_solution(screen, board):
    for col in range(len(board)):
        for p in range(len(board[col])):
            clr = fcolor(board, col, p)
            if board[col][p] == -1:
                clr = C_BOMBS
            pygame.draw.circle(screen, clr, (col * 100 + 100, p * 100 + 100), 40)

def render(screen, board, uncovered):
    for col in range(len(board)):
        for p in range(len(board[col])):
            pos =  (col * 100 + 100, p * 100 + 100)
            if (col, p) in uncovered:
                clr = fcolor(board, col, p)
                if board[col][p] == -1:
                    clr = C_BOMBS
                pygame.draw.circle(screen, clr, pos, 40)
            else:
                pygame.draw.circle(screen, (250, 250, 250), pos, 40)
            if (col, p) in flags:
                pygame.draw.circle(screen, FLAGS_C, pos, 30)

# INITIALIZE BOMBS

board, bombs = populate(board, N_BOMBS)
print(f"Number of bombs: {len(bombs)}")

for bomb in bombs:
    for j in PROXIM:
        try:
            if board[bomb[0] + j[0]][bomb[1] + j[1]] != -1 and bomb[0] + j[0] >= 0 and bomb[1] + j[1] >= 0:
                board[bomb[0] + j[0]][bomb[1] + j[1]] += 1
        except:
            pass

# MAIN

while game:
    clock.tick(fps)
    screen.fill("white")
    
    render(screen, board, uncovered)
    get_events()
    
    if pygame.mouse.get_pressed(3)[0] and not prev:
        prev = True
        pos = pygame.mouse.get_pos()
        posx = round((pos[0] - 100) / 100)
        posy = round((pos[1] - 100) / 100)
        try:
            if board[posx][posy] == 0:
                uncovered = uncover_neighbors(board, uncovered, (posx, posy))
            else:
                if (posx, posy) in flags:
                    uncovered.append((posx, posy))
                    flags.remove((posx, posy))
                    if (posx, posy) in bombs:
                        game = False
                elif not (posx, posy) in uncovered:
                    flags.append((posx, posy))
        except:
            pass
    if not pygame.mouse.get_pressed(3)[0]:
        prev = False
    
    flags_ratio = (len(flags)/N_BOMBS + flags_ratio * 5) / 6
    
    # Render flag progress
    pygame.draw.line(screen, (200, 200, 200), (flags_bg_start, flags_bg_height), (flags_bg_end, flags_bg_height), 10)
    pygame.draw.circle(screen, (200, 200, 200), (flags_bg_start, flags_bg_height +1), 5)
    pygame.draw.circle(screen, (200, 200, 200), (flags_bg_end, flags_bg_height +1), 5)
    pygame.draw.line(screen, FLAGS_C, (flags_bg_start, flags_bg_height), (flags_bg_start + int(flags_bg_width * flags_ratio), flags_bg_height), 10)
    pygame.draw.circle(screen, FLAGS_C, (flags_bg_start, flags_bg_height +1), 5)
    pygame.draw.circle(screen, FLAGS_C, (flags_bg_start + int(flags_bg_width * flags_ratio), flags_bg_height +1), 5)
    
    # win condition
    if len(flags) == N_BOMBS:
        win = True
        for i in flags:
            if not i in bombs:
                win = False
                break
        if not win:
            flags.clear()
        else:
            game = False
    pygame.display.flip()

c = 0
mx = 20
i = 0
particles = []
x = 0
y = 1

# LOSE ANIMATION

while not win:
   screen.fill("white")
   clock.tick(fps)
   
   render(screen, board, uncovered)
   get_events()
   
   c += 1
   if c > mx:
       try:
           c = 0
           uncovered.append(bombs[i])
           for j in range(20):
               ls = [(bombs[i][x] * 100 + 100, bombs[i][y] * 100 + 100), 20, (20 * (rf() - 0.5), 20 * (rf() - 0.5))]
               particles.append(ls)
           i += 1
       except:
           c = -1000
   
   for p in reversed(particles):
       pygame.draw.circle(screen, (200, 100, 120), p[0], p[1])
       p[0] = (p[0][x] + p[2][x], p[0][y] + p[2][y])
       p[1] = p[1] - 0.75
       if p[1] <= 0:
           particles.remove(p)
   pygame.display.flip()
   if c == -900:
       break

n_flags = len(flags)

# WIN ANIMATION

while win:
   screen.fill("white")
   render(screen, board, uncovered)
   clock.tick(fps)
   get_events()
   
   c+=1
   if c > mx:
       try:
           c = 0
           uncovered.append(flags[i])
           ls = [(bombs[i][x] * 100 + 100, bombs[i][y] * 100 + 100), 0]
           particles.append(ls)
           flags[i] = (-5, -5)
           i += 1
           n_flags -= 1
       except:
           c = -1000
   
   for p in particles:
       if p[1] < 50:
           p[1] += abs(50 - p[1]) * 0.2
       pygame.draw.circle(screen, (125, 200, 150), p[0], p[1])
   
   flags_ratio = (n_flags/N_BOMBS + 5 * flags_ratio) / 6
    
   pygame.draw.line(screen, (200, 200, 200), (flags_bg_start, flags_bg_height), (flags_bg_end, flags_bg_height), 10)
   pygame.draw.circle(screen, (200, 200, 200), (flags_bg_start, flags_bg_height +1), 5)
   pygame.draw.circle(screen, (200, 200, 200), (flags_bg_end, flags_bg_height +1), 5)
   pygame.draw.line(screen, FLAGS_C, (flags_bg_start, flags_bg_height), (flags_bg_start + int(flags_bg_width * flags_ratio), flags_bg_height), 10)
   pygame.draw.circle(screen, FLAGS_C, (flags_bg_start, flags_bg_height +1), 5)
   pygame.draw.circle(screen, FLAGS_C, (flags_bg_start + int(flags_bg_width * flags_ratio), flags_bg_height +1), 5)
    
   
   
   if c == -900:
       win = False
       break
   
   pygame.display.flip()