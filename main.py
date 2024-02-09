import pygame
from sys import exit

# pygame setup
pygame.init()
screen = pygame.display.set_mode((900, 720))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Skelly Runner")

# Init surfs
sky_surf = pygame.image.load('./images/level/bigsky.png').convert_alpha()
ground_surf = pygame.image.load('./images/level/ground.png').convert_alpha()


# FUNCTIONS
# def animations():
#     global sky_surf, sky_surf_1, sky_surf_2, sky_index
#
#     sky_index += 0.1
#     if sky_index >= len(sky_animation):
#         sky_index = 0
#     sky_surf = sky_animation[int(sky_index)]


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
            if colorkey is -1:
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

    # RENDER YOUR GAME HERE

    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 600))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
