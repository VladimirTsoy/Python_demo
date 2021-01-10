import simple_draw as sd


def draw_smile(x, y, radius=50, color=sd.COLOR_YELLOW, width=1):
    sd.circle(sd.get_point(x, y), radius, color, width)
    sd.circle(sd.get_point(x - radius / 2.0, y + radius / 2.0), radius / 8.0, color, width)
    sd.circle(sd.get_point(x + radius / 2.0, y + radius / 2.0), radius / 8.0, color, width)
    sd.line(sd.get_point(x - radius / 1.7, y - radius / 2.7), sd.get_point(x + radius / 1.7, y - radius / 2.7), color)


def smile_blink(x, y, radius=50, color=sd.COLOR_YELLOW, width=1):
    """ Рисование смайлика с закрытым правым глазом """

    sd.circle(sd.get_point(x, y), radius, color, width)
    sd.circle(sd.get_point(x - radius / 2.0, y + radius / 2.0), radius / 8.0, color, width)
    sd.line(sd.get_point(x - radius / 1.7, y - radius / 2.7), sd.get_point(x + radius / 1.7, y - radius / 2.7), color)
    blink_eye = sd.get_vector(sd.get_point(x + 7.0 * radius / 16.0, y + radius / 2.0), 0, radius / 4.0)
    blink_eye.draw(color)


def flashing_smiley(x, y, radius=50, color=sd.COLOR_YELLOW, width=1):
    num = sd.random_number(0, 1)
    if num == 0:
        smile_blink(x, y, radius, sd.background_color, width)
        draw_smile(x, y, radius, color, width)
    else:
        draw_smile(x, y, radius, sd.background_color, width)
        smile_blink(x, y, radius, color, width)
