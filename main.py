import sys
import pygame
from player import Plane, create_player
from round import Round, create_round
from enemy import Enemy, create_enemy


class Game:
    pass


def show_text(screen, x, y, font, msg, color,):
    text = font.render(msg, True, color)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)


FPS = 60
SPAWN_ENEMIES_EVENT = pygame.USEREVENT + 1
pygame.init()
pygame.font.init()
counter_font = pygame.font.SysFont(None, 30)
lose_font = pygame.font.SysFont(None, 70)
pygame.time.set_timer(pygame.USEREVENT, 250)
pygame.time.set_timer(SPAWN_ENEMIES_EVENT, 350)
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
player = pygame.sprite.Group()
rounds = pygame.sprite.Group()
enemies = pygame.sprite.Group()
plane = create_player(player)
create_round(rounds, plane.rect.x + (plane.rect.width / 2) - 10)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(1)
        if event.type == pygame.USEREVENT:
            if plane.alive:
                create_round(rounds, plane.rect.x + (plane.rect.width / 2) - 10)
        if event.type == SPAWN_ENEMIES_EVENT:
            create_enemy(enemies)
    screen.fill((0, 0, 0))
    player.draw(screen)
    rounds.draw(screen)
    enemies.draw(screen)
    enemies.update(screen_size)
    rounds.update(enemies, plane, screen_size)
    player.update(event)
    plane.collide_with_enemies(enemies)
    show_text(screen, 550, 20, counter_font, f"Врагов убито: {plane.kill_count}", (255, 255, 255))
    if not plane.alive:
        show_text(screen, 330, 240, lose_font, "WASTED", (255, 0, 0))
    pygame.display.update()
    clock.tick(FPS)
