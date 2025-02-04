import sys
import pygame
import sqlite3
from player import create_player
from round import create_round
from enemy import create_enemy
from menu import Menu
from finish_screen import FinishScreen
from utils import show_text


FPS = 60
pygame.mixer.init()
pygame.mixer.music.load('media/game.mp3')
pygame.mixer.music.play()
pygame.mixer.music.play(-1)
SPAWN_ENEMIES_EVENT = pygame.USEREVENT + 1
pygame.init()
pygame.font.init()
counter_font = pygame.font.SysFont(None, 30)
lose_font = pygame.font.SysFont(None, 70)
screen_size = (640, 480)
pygame.display.set_caption("Небесные тузы")
sky_img = pygame.image.load("media/sky.jpg")
plane_img = pygame.image.load('media/plane.jpg')
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
player = pygame.sprite.Group()
rounds = pygame.sprite.Group()
enemies = pygame.sprite.Group()
explosions = pygame.sprite.Group()
menu = Menu(screen, counter_font)
pygame.time.set_timer(pygame.USEREVENT, 250)
pygame.time.set_timer(SPAWN_ENEMIES_EVENT, 200)
plane = create_player(player)
finish_screen = FinishScreen(screen, menu, plane, lose_font)
connection = sqlite3.connect("records.db")
cursor = connection.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS
    Records (id INTEGER PRIMARY KEY, last_record INTEGER)
    """
)
last_record = cursor.execute(
    """SELECT last_record FROM Records WHERE id=?""", (1,)
).fetchone()
if not last_record:
    cursor.execute(
        """INSERT INTO Records (id, last_record) VALUES (?, ?)""",
        (1, 0)
    )
    last_record = 0
else:
    last_record = last_record[0]
connection.commit()
connection.close()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(1)
        if menu.is_started:
            if plane.alive:
                if event.type == pygame.USEREVENT:
                    if plane.alive:
                        create_round(
                            rounds, plane.rect.x + (plane.rect.width / 2)
                        )
                if event.type == SPAWN_ENEMIES_EVENT:
                    if plane.alive:
                        create_enemy(enemies)
            else:
                if event.type == pygame.MOUSEMOTION:
                    finish_screen.check_mouse_motion(event.pos)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    finish_screen.check_mouse_down(event.pos)
                if event.type == pygame.MOUSEBUTTONUP:
                    finish_screen.check_mouse_up()
        else:
            if event.type == pygame.MOUSEMOTION:
                menu.check_mouse_motion(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu.check_mouse_down(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                menu.check_mouse_up()
    screen.fill((0, 0, 0))
    if menu.is_started:
        if plane.alive:
            screen.blit(sky_img, (0, 0))
            player.draw(screen)
        rounds.draw(screen)
        enemies.draw(screen)
        explosions.draw(screen)
        enemies.update(screen_size)
        explosions.update()
        rounds.update(enemies, explosions, plane, screen_size)
        player.update(event)
        plane.collide_with_enemies(enemies)
        show_text(
            screen,
            550,
            20,
            counter_font,
            f"Врагов убито: {plane.kill_count}",
            (255, 255, 255),
        )
        if not plane.alive:

            screen.blit(plane_img, (0, 0))
            if plane.kill_count > last_record:
                connection = sqlite3.connect("records.db")
                cursor = connection.cursor()
                connection.commit()
                cursor.execute(
                    """UPDATE Records SET last_record = ? WHERE id=?""",
                    (plane.kill_count, 1),
                )
                connection.commit()
                connection.close()
                last_record = max(plane.kill_count, last_record)
            plane.kill_count = 0
            finish_screen.render()
    else:
        screen.blit(sky_img, (0, 0))
        menu.render(last_record)
    pygame.display.update()
    clock.tick(FPS)
