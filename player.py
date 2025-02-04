import pygame


class Plane(pygame.sprite.Sprite):
    def __init__(self, x, speed, group):
        super().__init__(group)
        self.image = pygame.image.load('plane.png').convert_alpha()
        self.rect = self.image.get_rect(center=(x, 440))
        self.speed = speed

    def update(self, event):
        speed = 0
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                speed = -self.speed
            if event.key in [pygame.K_RIGHT, pygame.K_d]:
                speed = abs(self.speed)
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_a] or event.key in [pygame.K_RIGHT, pygame.K_d]:
                speed = 0
        if 60 < self.rect.x < 480 - 60:
            self.rect.x += speed


def create_player(group):
    return Plane(240, 5, group)
