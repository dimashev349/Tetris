import pygame
import random

def make_noise():
    list_files = ["noise\\bruh.mp3",
                  "noise\\akh.mp3",
                  "noise\\bad-to-the-bone.mp3",
                  "noise\\fartmeme.mp3"]

    file = random.choice(list_files)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)
