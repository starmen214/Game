import pygame
from explosion import Explosion


class Round(pygame.sprite.Sprite):
    def __init__(self, x, speed, group):
        super().__init__(group)
        self.speed = speed
        self.image = pygame.image.load("media/round.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, 410))
        self.add(group)

    def update(self, enemy_group, explosions_group, plane, *args):
        if self.rect.y > 0:
            self.rect.y -= self.speed
        else:
            self.kill()
        for enemy in enemy_group:
            if self.rect.colliderect(enemy.rect):
                explosions_group.add(Explosion(enemy.rect.center, 'lg'))
                enemy.kill()
                plane.kill_count += 1


def create_round(group, x):
    return Round(x, 10, group)
