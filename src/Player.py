#!/usr/bin/env python3
##
## CREATIVE LAB PROJECT, 2022
## Yannis Defontaine
## File description:
## Pong game, play with your hands
##

import pygame
from pong import WINDOW_WIDTH, CAMERA_WIDTH, player_one_skin

Y = 1
X = 0

class Player:
    """
        Player is a bar who can move with your hand
    """
    def __init__(self, position: tuple = (10, 10), size: tuple = (25, 100), speed: int = 10, link_img: str = player_one_skin) -> None:
        self.pos = {
            'X': position[X],
            'Y': position[Y]
        }
        self.size = {
            'X': size[X],
            'Y': size[Y]
        }
        self.speed = speed
        self.skin = pygame.image.load(link_img)
        self.score = 0

    def draw(self, screen):
        screen.blit(self.skin, (self.pos['X'], self.pos['Y']))

    def move(self, bonus: int):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
           self.pos['Y'] -= self.speed + bonus
        if key[pygame.K_DOWN]:
           self.pos['Y'] += self.speed + bonus

    def update(self, screen, bonus: int = 0):
        self.pos['Y'] *= WINDOW_WIDTH / CAMERA_WIDTH
        self.pos['Y'] = min(self.pos['Y'], 2000)
        self.draw(screen)
