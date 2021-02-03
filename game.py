import pygame, sys, random

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 450))
    screen.blit(floor_surface, (floor_x_pos + 288, 450))

def create_pipe():
    pipe_ht = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (288, pipe_ht))
    top_pipe = pipe_surface.get_rect(midbottom = (288, pipe_ht - 150))
    return top_pipe, bottom_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 2
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 512:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()

#Game Variables
gravity = 0.125
bird_movement = 0

bg_surface = pygame.image.load("assets/background-day.png").convert()

floor_surface = pygame.image.load("assets/base.png").convert()

bird_surface = pygame.image.load("assets/redbird-midflap.png").convert()
bird_rect = bird_surface.get_rect(center = (50, 256))

pipe_surface = pygame.image.load("assets/pipe-green.png").convert()
pipe_list = []

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [200, 300, 400]

floor_x_pos = 0

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 6
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
    
    #Bird

    bird_movement += gravity
    bird_rect.centery += bird_movement

    screen.blit(bg_surface, (0, 0))
    screen.blit(bird_surface, bird_rect)

    #Pipes

    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)


    #Floor
    draw_floor()

    floor_x_pos -= 0.5

    if floor_x_pos <= -288:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)