import simple_draw as sd
import math as mt


def draw_beam(center, radius, start_angle, delta_angle=30, color=sd.COLOR_YELLOW, width=2):
    """ Функция рисования лучей для солнца """

    for angle in range(start_angle, start_angle + 360, delta_angle):
        x = center.x + radius * mt.cos(angle * mt.pi / 180)
        y = center.y + radius * mt.sin(angle * mt.pi / 180)
        beam = sd.get_vector(sd.get_point(x, y), angle, radius / 2.0, width)
        beam.draw(color)


def draw_sun(center, radius, color=sd.COLOR_YELLOW, width=2, start_angle=0):
    """ Функция рисования солнца """

    sd.circle(center, radius, color, 0)
    draw_beam(center, radius, start_angle, 30, color, width)


def shimmers_sun(center, radius, start_angle, delta_angle=30, color=sd.COLOR_YELLOW, width=2):
    """ Функция рисования солнца с переливающимися лучами """
    sd.circle(center, radius, color, 0)

    movie_angle = 15                # Углол, на который будем сдвигать лучики

    # Сначала затираем предыдущие лучики цветом фона
    start_angle -= movie_angle
    draw_beam(center, radius, start_angle, delta_angle, sd.background_color, width)

    # Теперь рисуем новые лучи желтым цветом
    start_angle += movie_angle
    draw_beam(center, radius, start_angle, delta_angle, color, width)

    return start_angle + movie_angle
