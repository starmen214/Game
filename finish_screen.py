from button import Button
from utils import show_text


class FinishScreen:
    def __init__(self, screen, menu, player, font):
        self.is_started = False
        self.play_again_btn = Button(
            330,
            280,
            170,
            50,
            "Играть снова",
            screen,
            (255, 255, 255),
            (255, 255, 255),
            (255, 255, 255),
            3,
            25,
            self.play_again,
            center_text=True,
        )
        self.to_menu_btn = Button(
            160,
            280,
            100,
            50,
            "В меню",
            screen,
            (255, 255, 255),
            (255, 255, 255),
            (255, 255, 255),
            3,
            25,
            self.to_menu,
            center_text=True,
        )
        self.screen = screen
        self.font = font
        self.menu_class = menu
        self.player_class = player
        self.buttons = [self.to_menu_btn, self.play_again_btn]

    def play_again(self):
        self.player_class.alive = True
        self.menu_class.is_started = True

    def to_menu(self):
        self.player_class.alive = True
        self.menu_class.is_started = False

    def finish_screen_check_mouse_down(self, pos):
        for btn in self.buttons:
            btn.check_mouse_down(pos)

    def finish_screen_check_mouse_up(self):
        for btn in self.buttons:
            btn.check_mouse_up()

    def finish_screen_check_mouse_motion(self, pos):
        for btn in self.buttons:
            btn.check_mouse_motion(pos)

    def render(self):
        show_text(self.screen, 330, 240, self.font, "ВЫ ПОГИБЛИ", (255, 255, 255))
        self.play_again_btn.render()
        self.to_menu_btn.render()

    def check_mouse_motion(self, pos):
        for btn in self.buttons:
            btn.check_mouse_motion(pos)

    def check_mouse_down(self, pos):
        for btn in self.buttons:
            btn.check_mouse_down(pos)

    def check_mouse_up(self):
        for btn in self.buttons:
            btn.check_mouse_up()
