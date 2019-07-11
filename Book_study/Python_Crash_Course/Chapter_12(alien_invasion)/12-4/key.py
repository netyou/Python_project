import pygame
import sys


def check_key():

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(event)

        elif event.type == pygame.QUIT:
            sys.exit()




