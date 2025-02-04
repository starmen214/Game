import pygame
from button import Button
from utils import show_text


class Menu:
    def __init__(self, screen, font):
        self.is_started = False
        self.choosing_level = False
        self.start_button = Button(
            270,
            200,
            100,
            50,
            "Начать",
            screen,
            (255, 0, 0),
            (255, 255, 255),
            (255, 50, 50),
            3,
            25,
            self.start_game,
            center_text=True,
        )
        self.exit_button = Button(
            270,
            280,
            100,
            50,
            "Выйти",
            screen,
            (255, 0, 0),
            (255, 255, 255),
            (255, 50, 50),
            3,
            25,
            self.exit_game,
            center_text=True,
        )
        self.easy_button = Button(
            270,
            200,
            120,
            50,
            "Лёгкая",
            screen,
            (255, 0, 0),
            (255, 255, 255),
            (255, 50, 50),
            3,
            25,
            self.set_easy,
            center_text=True,
        )
        self.norm_button = Button(
            270,
            280,
            120,
            50,
            "Средняя",
            screen,
            (255, 0, 0),
            (255, 255, 255),
            (255, 50, 50),
            3,
            25,
            self.set_normal,
            center_text=True,
        )
        self.hard_button = Button(
            270,
            350,
            120,
            50,
            "Хардкор",
            screen,
            (255, 0, 0),
            (255, 255, 255),
            (255, 50, 50),
            3,
            25,
            self.set_hard,
            center_text=True,
        )
        self.screen = screen
        self.font = font
        self.start_buttons = [self.start_button, self.exit_button]
        self.level_buttons = [
            self.easy_button, self.norm_button, self.hard_button
        ]

    def exit_game(self):
        exit(1)

    def start_game(self):
        self.choosing_level = True

    def set_easy(self):
        pygame.time.set_timer(pygame.USEREVENT, 100)
        pygame.time.set_timer(pygame.USEREVENT + 1, 300)
        self.choosing_level = False
        self.is_started = True

    def set_normal(self):
        pygame.time.set_timer(pygame.USEREVENT, 200)
        pygame.time.set_timer(pygame.USEREVENT + 1, 250)
        self.choosing_level = False
        self.is_started = True

    def set_hard(self):
        pygame.time.set_timer(pygame.USEREVENT, 350)
        pygame.time.set_timer(pygame.USEREVENT + 1, 100)
        self.choosing_level = False
        self.is_started = True

    def render(self, last_record):
        if not self.choosing_level:
            self.start_button.render()
            self.exit_button.render()
            show_text(
                self.screen,
                320,
                150,
                self.font,
                f'Последний рекорд: {last_record}',
                (255, 255, 255)
            )
        else:
            self.easy_button.render()
            self.norm_button.render()
            self.hard_button.render()
            show_text(
                self.screen,
                320,
                80,
                self.font,
                'Выберите сложность:',
                (255, 255, 255)
            )

    def check_mouse_motion(self, pos):
        if not self.choosing_level:
            for btn in self.start_buttons:
                btn.check_mouse_motion(pos)
        else:
            for btn in self.level_buttons:
                btn.check_mouse_motion(pos)

    def check_mouse_down(self, pos):
        if not self.choosing_level:
            for btn in self.start_buttons:
                btn.check_mouse_down(pos)
        else:
            for btn in self.level_buttons:
                btn.check_mouse_down(pos)

    def check_mouse_up(self):
        if not self.choosing_level:
            for btn in self.start_buttons:
                btn.check_mouse_up()
        else:
            for btn in self.level_buttons:
                btn.check_mouse_up()
