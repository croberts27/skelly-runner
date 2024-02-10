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


# FUNCTIONS
def animations():
    global sky_surf, ground_surf, sky_rect, ground_rect

    # Move the sky horizontally
    sky_rect.x -= 1  # Adjust the speed
    # If the sky has moved completely off-screen, reset its position
    if sky_rect.right <= 0:
        sky_rect.x = 900  # Adjust the initial position based on your screen size
    # Move the ground horizontally at a slower speed
    ground_rect.x -= 3  # Adjust the speed as needed
    # If the ground has moved completely off-screen, reset its position
    if ground_rect.x <= -90:
        ground_rect.x = 0  # Reset to the original position



# CLASSES
class SpriteSheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as message:
            print('Unable to load sprite sheet image:', filename)
            raise SystemExit(message)

    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey=None):
        """Loads image from x,y,x+offset,y+offset"""
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    # Load a bunch of images and return them as a list
    def images_at(self, rects, colorkey=None):
        """Loads multiple images, supply a list of coordinates"""
        return [self.image_at(rect, colorkey) for rect in rects]

    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey=None):
        """Loads a strip of images and returns them as a list"""
        tups = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    animations()

    screen.fill((102, 113, 159))

    # RENDER YOUR GAME HERE
    screen.blit(sky_surf, sky_rect)
    screen.blit(ground_surf, ground_rect)
    screen.blit(title, title_rect)
    screen.blit(title_2, title_2_rect)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
