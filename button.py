import pygame


class Button:
    def __init__(
        self,
        x,
        y,
        w,
        h,
        text,
        surface,
        bcolor,
        tcolor,
        hcolor,
        border,
        tsize,
        func,
        center_text=False,
    ):
        self.font = pygame.font.SysFont(None, tsize)
        self.bound = pygame.Rect(x, y, w, h)
        self.h = h
        self.w = w
        self.tsize = tsize
        self.text = str(text)
        self.surface = surface
        self.button_color = bcolor
        self.text_color = tcolor
        self.hover_color = hcolor
        self.border = border
        self.state = "normal"
        self.on_click_func = func
        self.centralize_text = center_text

    def render(self):
        if self.state == "normal":
            pygame.draw.rect(self.surface, self.button_color, self.bound, self.border)
            self.render_text(self.bound.x + 2, self.bound.y + 5)
        else:
            pygame.draw.rect(self.surface, self.hover_color, self.bound, self.border)
            self.render_text(self.bound.x + 2, self.bound.y + 5)

    def render_text(self, x, y):
        if self.centralize_text:
            text_object = self.font.render(self.text, True, self.text_color)
            self.surface.blit(
                text_object,
                (x + self.tsize, y + self.h // 2 - self.tsize // 2),
            )
        else:
            text_object = self.font.render(self.text, True, self.text_color)
            self.surface.blit(text_object, (x, y))

    def check_mouse_motion(self, pos):
        if self.bound.collidepoint(pos[0], pos[1]):
            if self.state != "pressed":
                self.state = "hover"
        else:
            self.state = "normal"

    def check_mouse_down(self, pos):
        if self.bound.collidepoint(pos[0], pos[1]):
            self.state = "pressed"

    def check_mouse_up(self):
        if self.state == "pressed":
            self.on_click()
            self.state = "hover"

    def on_click(self):
        self.on_click_func()

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = str(text)

    def get_coords(self):
        return self.bound.x, self.bound.y, self.bound.w, self.bound.h

    def set_coords(self, coords, tsize):
        self.font = pygame.font.SysFont("Montserrat", tsize)
        x, y, w, h = coords
        self.bound = pygame.Rect(x, y, w, h)
