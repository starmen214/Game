import pygame


class Round(pygame.sprite.Sprite):
    def __init__(self, x, speed, group):
        super().__init__(group)
        self.speed = speed
        self.image = pygame.image.load('round.png').convert_alpha()
        self.rect = self.image.get_rect(center=(x, 410))
        self.add(group)

    def update(self, *args):
        if self.rect.y < args[0][1]:
            self.rect.y -= self.speed
        else:
            self.kill()


def create_round(group, x):
    return Round(x, 10, group)
