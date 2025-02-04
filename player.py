import pygame


class Plane(pygame.sprite.Sprite):
    def __init__(self, x, speed, group):
        super().__init__(group)
        self.image = pygame.image.load("media/plane.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, 440))
        self.speed = speed
        self.can_move = True
        self.vx = 0
        self.kill_count = 0
        self.alive = True

    def update(self, event):
        if self.can_move:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.move_left()
                elif event.key == pygame.K_LEFT:
                    self.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.move_right()
                elif event.key == pygame.K_d:
                    self.move_right()
                else:
                    self.vx = 0
                self.rect.x += self.vx

    def collide_with_enemies(self, enemy_group):
        for enemy in enemy_group:
            if self.rect.colliderect(enemy.rect):
                self.alive = False

    def move_left(self):
        if self.rect.x > 0:
            self.vx = -self.speed
        else:
            self.vx = 0

    def move_right(self):
        if self.rect.x < (640 - self.rect.width):
            self.vx = self.speed
        else:
            self.vx = 0

    def check(self):
        if 0 <= self.rect.x <= 640 - self.rect.width:
            return False
        else:
            self.can_move = False
        return True


def create_player(group):
    return Plane(240, 5, group)
