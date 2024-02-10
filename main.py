import pygame
from sys import exit

# pygame setup
pygame.init()
screen = pygame.display.set_mode((900, 720))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Skelly Runner")

font_1 = pygame.font.Font('fonts/skellyfont.ttf', 60)
font_2 = pygame.font.Font('fonts/skellyfont_other.ttf', 60)

title = font_1.render('Skelly Runner', False, 'white')
title_2 = font_2.render('Skelly Runner', False, 'black')
title_rect = title.get_rect(center=(450, 75))
title_2_rect = title_2.get_rect(center=(450, 75))

# Init surfs
sky_surf_1 = pygame.image.load('./images/level/sky1.png').convert_alpha()
sky_surf_2 = pygame.image.load('./images/level/sky2.png').convert_alpha()
sky_surf_3 = pygame.image.load('./images/level/sky3.png').convert_alpha()
sky_surf_4 = pygame.image.load('./images/level/sky4.png').convert_alpha()
sky_surf_5 = pygame.image.load('./images/level/sky5.png').convert_alpha()
sky_index = 0
sky_animation = [sky_surf_1, sky_surf_2, sky_surf_3, sky_surf_4, sky_surf_5]

sky_surf = sky_animation[sky_index]
sky_rect = sky_surf.get_rect(center=(800, 500))
ground_surf = pygame.image.load('./images/level/ground.png').convert_alpha()
ground_rect = ground_surf.get_rect(bottomright=(0, 730))

# player surfs
player_walk_1 = pygame.image.load('images/player/walk/walk_1.png').convert_alpha()
player_walk_1 = pygame.transform.rotozoom(player_walk_1, 0, 2)
player_walk_2 = pygame.image.load('images/player/walk/walk_2.png').convert_alpha()
player_walk_2 = pygame.transform.rotozoom(player_walk_2, 0, 2)
player_walk_3 = pygame.image.load('images/player/walk/walk_3.png').convert_alpha()
player_walk_3 = pygame.transform.rotozoom(player_walk_3, 0, 2)
player_walk_4 = pygame.image.load('images/player/walk/walk_4.png').convert_alpha()
player_walk_4 = pygame.transform.rotozoom(player_walk_4, 0, 2)
player_walk_5 = pygame.image.load('images/player/walk/walk_5.png').convert_alpha()
player_walk_5 = pygame.transform.rotozoom(player_walk_5, 0, 2)
player_walk_6 = pygame.image.load('images/player/walk/walk_6.png').convert_alpha()
player_walk_6 = pygame.transform.rotozoom(player_walk_6, 0, 2)
player_walk_7 = pygame.image.load('images/player/walk/walk_7.png').convert_alpha()
player_walk_7 = pygame.transform.rotozoom(player_walk_7, 0, 2)
player_walk_8 = pygame.image.load('images/player/walk/walk_8.png').convert_alpha()
player_walk_8 = pygame.transform.rotozoom(player_walk_8, 0, 2)
player_walk_9 = pygame.image.load('images/player/walk/walk_9.png').convert_alpha()
player_walk_9 = pygame.transform.rotozoom(player_walk_9, 0, 2)
player_walk = [player_walk_1, player_walk_2, player_walk_3, player_walk_4, player_walk_5, player_walk_6, player_walk_7, player_walk_8, player_walk_9]

# player jump
player_index = 0

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(100, 615))
player_gravity = 0

# FUNCTIONS
def background_animations():
    global sky_surf, ground_surf, sky_rect, ground_rect

    # Move the sky horizontally
    sky_rect.x -= 1
    # If the sky has moved completely off-screen, reset its position
    if sky_rect.right <= 0:
        sky_rect.x = 900
    # Move the ground horizontally at a slower speed
    ground_rect.x -= 3
    # If the ground has moved completely off-screen, reset its position
    if ground_rect.x <= -85:
        ground_rect.x = 0  # Reset to the original position

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 345:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]
    # player walking animation if player is on the floor
    # display jump surface when player is not on floor

# CLASSES


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        if running:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 345:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
            if event.type == pygame.KEYDOWN and player_rect.bottom >= 345:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    background_animations()

    screen.fill((102, 113, 159))

    # RENDER YOUR GAME HERE
    screen.blit(sky_surf, sky_rect)
    screen.blit(ground_surf, ground_rect)
    screen.blit(title, title_rect)
    screen.blit(title_2, title_2_rect)
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 615:
        player_rect.bottom = 615
    player_animation()
    screen.blit(player_surf, player_rect)



    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
