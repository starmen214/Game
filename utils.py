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
