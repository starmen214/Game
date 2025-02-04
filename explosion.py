import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.explosion_animation = self.load_images()
        self.image = self.explosion_animation[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion_animation[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosion_animation[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def load_images(self):
        explosion_animation = {}
        explosion_animation['lg'] = []
        explosion_animation['sm'] = []
        for i in range(9):
            filename = 'regularExplosion0{}.png'.format(i)
            img = pygame.image.load('media/Explosions/' + filename).convert()
            img.set_colorkey((0, 0, 0))
            img_lg = pygame.transform.scale(img, (75, 75))
            explosion_animation['lg'].append(img_lg)
            img_sm = pygame.transform.scale(img, (32, 32))
            explosion_animation['sm'].append(img_sm)
        return explosion_animation
