from button import Button
from utils import show_text


class Menu:
    def __init__(self, screen, font):
        self.is_started = False
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
        self.screen = screen
        self.font = font
        self.buttons = [self.start_button, self.exit_button]

    def exit_game(self):
        exit(1)

    def start_game(self):
        self.is_started = True

    def render(self, last_record):
        self.start_button.render()
        self.exit_button.render()
        show_text(self.screen, 320, 150, self.font, f'Последний рекорд: {last_record}', (255, 255, 255))

    def check_mouse_motion(self, pos):
        for btn in self.buttons:
            btn.check_mouse_motion(pos)

    def check_mouse_down(self, pos):
        for btn in self.buttons:
            btn.check_mouse_down(pos)

    def check_mouse_up(self):
        for btn in self.buttons:
            btn.check_mouse_up()
