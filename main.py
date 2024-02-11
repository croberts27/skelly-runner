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


# CLASSES
class Player:
    def __init__(self):
        # player surfs
        self.player_walk_1 = pygame.image.load('images/player/walk/walk_1.png').convert_alpha()
        self.player_walk_1 = pygame.transform.rotozoom(self.player_walk_1, 0, 2)
        self.player_walk_2 = pygame.image.load('images/player/walk/walk_2.png').convert_alpha()
        self.player_walk_2 = pygame.transform.rotozoom(self.player_walk_2, 0, 2)
        self.player_walk_3 = pygame.image.load('images/player/walk/walk_3.png').convert_alpha()
        self.player_walk_3 = pygame.transform.rotozoom(self.player_walk_3, 0, 2)
        self.player_walk_4 = pygame.image.load('images/player/walk/walk_4.png').convert_alpha()
        self.player_walk_4 = pygame.transform.rotozoom(self.player_walk_4, 0, 2)
        self.player_walk_5 = pygame.image.load('images/player/walk/walk_5.png').convert_alpha()
        self.player_walk_5 = pygame.transform.rotozoom(self.player_walk_5, 0, 2)
        self.player_walk_6 = pygame.image.load('images/player/walk/walk_6.png').convert_alpha()
        self.player_walk_6 = pygame.transform.rotozoom(self.player_walk_6, 0, 2)
        self.player_walk_7 = pygame.image.load('images/player/walk/walk_7.png').convert_alpha()
        self.player_walk_7 = pygame.transform.rotozoom(self.player_walk_7, 0, 2)
        self.player_walk_8 = pygame.image.load('images/player/walk/walk_8.png').convert_alpha()
        self.player_walk_8 = pygame.transform.rotozoom(self.player_walk_8, 0, 2)
        self.player_walk_9 = pygame.image.load('images/player/walk/walk_9.png').convert_alpha()
        self.player_walk_9 = pygame.transform.rotozoom(self.player_walk_9, 0, 2)
        self.player_walk = [self.player_walk_1, self.player_walk_2, self.player_walk_3, self.player_walk_4,
                            self.player_walk_5, self.player_walk_6, self.player_walk_7,
                            self.player_walk_8, self.player_walk_9]

        self.player_jump_1 = pygame.image.load('images/player/jump/jump1.png').convert_alpha()
        self.player_jump_1 = pygame.transform.rotozoom(self.player_jump_1, 0, 2)
        self.player_jump_2 = pygame.image.load('images/player/jump/jump2.png').convert_alpha()
        self.player_jump_2 = pygame.transform.rotozoom(self.player_jump_2, 0, 2)
        self.player_jump_3 = pygame.image.load('images/player/jump/jump3.png').convert_alpha()
        self.player_jump_3 = pygame.transform.rotozoom(self.player_jump_3, 0, 2)
        self.player_jump_4 = pygame.image.load('images/player/jump/jump4.png').convert_alpha()
        self.player_jump_4 = pygame.transform.rotozoom(self.player_jump_4, 0, 2)
        self.player_jump_5 = pygame.image.load('images/player/jump/jump5.png').convert_alpha()
        self.player_jump_5 = pygame.transform.rotozoom(self.player_jump_5, 0, 2)
        self.player_jump_6 = pygame.image.load('images/player/jump/jump6.png').convert_alpha()
        self.player_jump_6 = pygame.transform.rotozoom(self.player_jump_6, 0, 2)
        self.player_jump_7 = pygame.image.load('images/player/jump/jump7.png').convert_alpha()
        self.player_jump_7 = pygame.transform.rotozoom(self.player_jump_7, 0, 2)
        self.player_jump = [self.player_jump_1, self.player_jump_2, self.player_jump_3, self.player_jump_4,
                            self.player_jump_5, self.player_jump_6, self.player_jump_7]

        self.player_index = 0

        self.player_surf = self.player_walk[self.player_index]
        self.player_rect = self.player_surf.get_rect(midbottom=(100, 615))
        self.player_gravity = 0

    def player_animation(self):
        if self.player_gravity < 0:  # Player is jumping
            self.player_index += 0.2
            if self.player_index >= len(self.player_jump):
                self.player_index = 0
            self.player_surf = self.player_jump[int(self.player_index)]
        elif self.player_rect.bottom < 615:  # Player is falling
            self.player_index = 0  # Reset the animation index
            self.player_surf = self.player_jump[0]  # Use the first frame of the jump animation
        else:  # Player is walking
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.player_surf = self.player_walk[int(self.player_index)]

    def jump(self):
        if self.player_rect.bottom >= 615:  # Check if the player is on the ground
            self.player_gravity = -20  # Apply an initial jump velocity


class Background:

    def __init__(self):
        # Init surfs
        self.sky_surf_1 = pygame.image.load('./images/level/sky1.png').convert_alpha()
        self.sky_surf_2 = pygame.image.load('./images/level/sky2.png').convert_alpha()
        self.sky_surf_3 = pygame.image.load('./images/level/sky3.png').convert_alpha()
        self.sky_surf_4 = pygame.image.load('./images/level/sky4.png').convert_alpha()
        self.sky_surf_5 = pygame.image.load('./images/level/sky5.png').convert_alpha()
        self.sky_index = 0
        self.sky_animation = [self.sky_surf_1, self.sky_surf_2, self.sky_surf_3, self.sky_surf_4, self.sky_surf_5]

        self.sky_surf = self.sky_animation[self.sky_index]
        self.sky_rect = self.sky_surf.get_rect(center=(800, 500))
        self.ground_surf = pygame.image.load('./images/level/ground.png').convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(bottomright=(0, 730))

    def background_animations(self):
        # Move the sky horizontally
        self.sky_rect.x -= 1
        # If the sky has moved completely off-screen, reset its position
        if self.sky_rect.right <= 0:
            self.sky_rect.x = 900
        # Move the ground horizontally at a slower speed
        self.ground_rect.x -= 2
        # If the ground has moved completely off-screen, reset its position
        if self.ground_rect.x <= -85:
            self.ground_rect.x = 0  # Reset to the original position


class Enemy:
    def __init__(self):
        super().__init__()
        self.enemy_walk_1 = pygame.image.load('images/enemy/walk/enemy_walk_1.png').convert_alpha()
        self.enemy_walk_1 = pygame.transform.rotozoom(self.enemy_walk_1, 0, 2)
        self.enemy_walk_2 = pygame.image.load('images/enemy/walk/enemy_walk_2.png').convert_alpha()
        self.enemy_walk_2 = pygame.transform.rotozoom(self.enemy_walk_2, 0, 2)
        self.enemy_walk_3 = pygame.image.load('images/enemy/walk/enemy_walk_3.png').convert_alpha()
        self.enemy_walk_3 = pygame.transform.rotozoom(self.enemy_walk_3, 0, 2)
        self.enemy_walk_4 = pygame.image.load('images/enemy/walk/enemy_walk_4.png').convert_alpha()
        self.enemy_walk_4 = pygame.transform.rotozoom(self.enemy_walk_4, 0, 2)
        self.enemy_walk_5 = pygame.image.load('images/enemy/walk/enemy_walk_5.png').convert_alpha()
        self.enemy_walk_5 = pygame.transform.rotozoom(self.enemy_walk_5, 0, 2)
        self.enemy_walk_6 = pygame.image.load('images/enemy/walk/enemy_walk_6.png').convert_alpha()
        self.enemy_walk_6 = pygame.transform.rotozoom(self.enemy_walk_6, 0, 2)
        self.enemy_walk_7 = pygame.image.load('images/enemy/walk/enemy_walk_7.png').convert_alpha()
        self.enemy_walk_7 = pygame.transform.rotozoom(self.enemy_walk_7, 0, 2)
        self.enemy_walk_8 = pygame.image.load('images/enemy/walk/enemy_walk_8.png').convert_alpha()
        self.enemy_walk_8 = pygame.transform.rotozoom(self.enemy_walk_8, 0, 2)
        self.enemy_walk_9 = pygame.image.load('images/enemy/walk/enemy_walk_9.png').convert_alpha()
        self.enemy_walk_9 = pygame.transform.rotozoom(self.enemy_walk_9, 0, 2)
        self.enemy_walk = [self.enemy_walk_1, self.enemy_walk_2, self.enemy_walk_3, self.enemy_walk_4,
                           self.enemy_walk_5, self.enemy_walk_6, self.enemy_walk_7, self.enemy_walk_8,
                           self.enemy_walk_9]
        self.enemy_index = 0
        self.enemy_attack_index = 0

        self.enemy_surf = self.enemy_walk[self.enemy_index]
        self.enemy_rect = self.enemy_surf.get_rect(midbottom=(800, 615))
        self.enemy_gravity = 0

        self.enemy_attack_1 = pygame.image.load('images/enemy/attack/img.png').convert_alpha()
        self.enemy_attack_1 = pygame.transform.rotozoom(self.enemy_attack_1, 0, 2)
        self.enemy_attack_2 = pygame.image.load('images/enemy/attack/img_1.png').convert_alpha()
        self.enemy_attack_2 = pygame.transform.rotozoom(self.enemy_attack_2, 0, 2)
        self.enemy_attack_3 = pygame.image.load('images/enemy/attack/img_2.png').convert_alpha()
        self.enemy_attack_3 = pygame.transform.rotozoom(self.enemy_attack_3, 0, 2)
        self.enemy_attack_4 = pygame.image.load('images/enemy/attack/img_3.png').convert_alpha()
        self.enemy_attack_4 = pygame.transform.rotozoom(self.enemy_attack_4, 0, 2)
        self.enemy_attack_5 = pygame.image.load('images/enemy/attack/img_4.png').convert_alpha()
        self.enemy_attack_5 = pygame.transform.rotozoom(self.enemy_attack_5, 0, 2)
        self.enemy_attack_6 = pygame.image.load('images/enemy/attack/img_5.png').convert_alpha()
        self.enemy_attack_6 = pygame.transform.rotozoom(self.enemy_attack_6, 0, 2)
        self.enemy_attack = [self.enemy_attack_1, self.enemy_attack_2, self.enemy_attack_3, self.enemy_attack_4,
                             self.enemy_attack_5, self.enemy_attack_6]
        self.enemy_attack_surf = self.enemy_attack[self.enemy_attack_index]
        self.enemy_attack_rect = self.enemy_attack_surf.get_rect(midbottom=(1200, 615))

    def enemy_animation(self):
        self.enemy_rect.bottom = 615
        self.enemy_index += 0.2
        if self.enemy_index >= len(self.enemy_walk):
            self.enemy_index = 0
        self.enemy_surf = self.enemy_walk[int(self.enemy_index)]
        self.enemy_rect.x -= 2
        if self.enemy_rect.right <= 0:
            self.enemy_rect.right = 1200
        if self.enemy_rect.left.colliderect()

    def enemy_attack_animation(self):
        self.enemy_attack_rect.bottom = 615
        self.enemy_attack_index += 0.2
        if self.enemy_attack_index >= len(self.enemy_attack):
            self.enemy_attack_index = 0
        self.enemy_attack_surf = self.enemy_attack[int(self.enemy_attack_index)]
        self.enemy_attack_rect.x -= 2
        if self.enemy_attack_rect.right <= 0:
            self.enemy_attack_rect.right = 1200


player = Player()

background = Background()

enemy = Enemy()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    background.background_animations()

    screen.fill((102, 113, 159))

    # RENDER YOUR GAME HERE
    screen.blit(background.sky_surf, background.sky_rect)
    screen.blit(background.ground_surf, background.ground_rect)
    screen.blit(title, title_rect)
    screen.blit(title_2, title_2_rect)
    player.player_gravity += 1
    player.player_rect.y += player.player_gravity  # Update player's position based on gravity
    if player.player_rect.bottom >= 615:
        player.player_rect.bottom = 615
    player.player_animation()
    screen.blit(player.player_surf, player.player_rect)
    enemy.enemy_animation()
    screen.blit(enemy.enemy_surf, enemy.enemy_rect)
    screen.blit(enemy.enemy_attack_surf, enemy.enemy_attack_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
exit()
