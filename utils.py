import sys
import os

def show_text(
    screen,
    x,
    y,
    font,
    msg,
    color,
):
    text = font.render(msg, True, color)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)