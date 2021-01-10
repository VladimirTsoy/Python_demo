# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

radius = 50  # Величина смайла


def draw_smile(x, y, color):
    sd.circle(sd.get_point(x, y), radius, color, 1)
    sd.circle(sd.get_point(x - radius / 2.0, y + radius / 2.0), radius / 8.0, color, 1)
    sd.circle(sd.get_point(x + radius / 2.0, y + radius / 2.0), radius / 8.0, color, 1)
    sd.line(sd.get_point(x - radius / 1.7, y - radius / 2.7), sd.get_point(x + radius / 1.7, y - radius / 2.7), color)


for _ in range(10):
    center = sd.random_point()
    draw_smile(center.x, center.y, sd.COLOR_YELLOW)
sd.pause()
# зачет!