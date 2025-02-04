import sys
import pygame
from player import Plane, create_player
from round import Round, create_round


class Game:
    pass


FPS = 60
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 130)
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
player = pygame.sprite.Group()
rounds = pygame.sprite.Group()
plane = create_player(player)
create_round(rounds, plane.rect.x + (plane.rect.width / 2) - 10)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(1)
        if event.type == pygame.USEREVENT:
            create_round(rounds, plane.rect.x + (plane.rect.width / 2) - 10)
    screen.fill((0, 0, 0))
    player.draw(screen)
    rounds.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
    rounds.update(screen_size)
    player.update(event)

