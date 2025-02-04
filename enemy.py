import pygame
from random import choice, randint


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, speed, group):
        super().__init__(group)
        self.speed = speed
        self.image = pygame.image.load(
            choice(["media/enemy1.png", "media/enemy2.png", "media/enemy3.png"])
        ).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))
        self.add(group)

    def update(self, *args):
        if self.rect.y < 480:
            self.rect.y += self.speed
        else:
            self.kill()


def create_enemy(group):
    return Enemy(randint(75, 565), 5, group)
