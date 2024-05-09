import pygame
import time
import random
from audio import make_noise

pygame.init()
pygame.mixer.init()

WIDTH_UI = 300
HEIGHT_UI = 30
W, H = 10, 20
TILE = 45
GAME_RES = W * TILE, H * TILE
display_info = pygame.display.Info()
RES = GAME_RES[0] + WIDTH_UI, GAME_RES[1] + HEIGHT_UI
sc = pygame.display.set_mode(RES)

duration = 3
def show_image():
    list_files = ["img\\fear\\boo.jpg",
                  "img\\fear\\boo2.jpg",
                  "img\\fear\\boo3.jpg",
                  "img\\fear\\boo4.jpg"]
    image_path = random.choice(list_files)
    image = pygame.image.load(image_path).convert()
    sc.blit(image, ((RES[0] - image.get_width()) // 2, (RES[1] - image.get_height()) // 2))
    pygame.display.flip()
    make_noise()
    time.sleep(duration)
    pygame.display.flip()

    time.sleep(duration)