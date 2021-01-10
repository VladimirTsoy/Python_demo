# -*- coding: utf-8 -*-
import simple_draw as sd
from lesson_005.results.draw_image import smile as sm


def draw_roof(left_bottom, right_top, color):
    """ Отрисовка крыши """

    len_visor = (right_top.x - left_bottom.x) / 4.0  # Длина козырька
    height_roof = (right_top.y - left_bottom.y) / 3.0  # Высота крыши

    roof_points = [sd.get_point(left_bottom.x - len_visor, right_top.y),  # Левая сторона крыши
                   sd.get_point(right_top.x + len_visor, right_top.y),  # Правая сторона крыши
                   sd.get_point((left_bottom.x + right_top.x) / 2.0, right_top.y + height_roof)]  # Верх

    sd.polygon(roof_points, color, 0)


def draw_window_smile(left_bottom, right_top, color_frame, width_frame=1, color_fon=sd.background_color):
    """ Отрисока окна и смайлика в нём """

    width_ident = (right_top.x - left_bottom.x) * 0.3  # Ширина отступа до окна
    height_ident = (right_top.y - left_bottom.y) * 0.2  # Высота от пола до окна
    bottom_window = sd.get_point(left_bottom.x + width_ident, left_bottom.y + height_ident)
    top_window = sd.get_point(right_top.x - width_ident, right_top.y - height_ident)
    sd.rectangle(bottom_window, top_window, color_fon, 0)
    sd.rectangle(bottom_window, top_window, color_frame, width_frame)
    x_smile = bottom_window.x + (top_window.x - bottom_window.x) / 2.0
    y_smile = bottom_window.y + (top_window.y - bottom_window.y) / 2.0
    sm.draw_smile(x_smile, y_smile, 20, sd.COLOR_YELLOW)


def draw_window(left_bottom, right_top, color_frame, width_frame=1, color_fon=sd.background_color):
    width_ident = (right_top.x - left_bottom.x) * 0.3  # Ширина отступа до окна
    height_ident = (right_top.y - left_bottom.y) * 0.2  # Высота от пола до окна
    bottom_window = sd.get_point(left_bottom.x + width_ident, left_bottom.y + height_ident)
    top_window = sd.get_point(right_top.x - width_ident, right_top.y - height_ident)
    sd.rectangle(bottom_window, top_window, color_fon, 0)
    sd.rectangle(bottom_window, top_window, color_frame, width_frame)


def draw_house(len_brick, height_brick, left_point, color=sd.COLOR_YELLOW, width=1, smile=1):
    """ Рисование дома с крышей, окном и смайликом в нём """

    n, m = 9, 15  # Количество кирпичиков в длину и высоту соотв.
    left_bottom = sd.get_point(left_point.x - len_brick, left_point.y)  # Левая нижняя точка кирпича
    right_top = sd.get_point(left_point.x, left_point.y + height_brick)  # Правая верхняя точка кирпича
    shift = len_brick / 2.0

    for i in range(1, m + 1):
        for j in range(n + 1):
            sd.rectangle(left_bottom, right_top, color, width)
            left_bottom.x += len_brick
            right_top.x += len_brick
        left_bottom.y += height_brick
        right_top.y += height_brick
        if i % 2:
            left_bottom.x = left_point.x - len_brick + shift
            right_top.x = left_point.x + shift
        else:
            left_bottom.x = left_point.x - len_brick
            right_top.x = left_point.x

        # Обрамляем рамкой стену
    left_bottom.x = left_point.x - len_brick
    left_bottom.y = left_point.y
    right_top.x = left_point.x + n * len_brick + shift
    right_top.y = left_point.y + m * height_brick
    sd.rectangle(left_bottom, right_top, color, width)

    draw_roof(left_bottom, right_top, sd.COLOR_ORANGE)  # Рисуем крышу

    if smile == 1:
        draw_window_smile(left_bottom, right_top, color, width)  # Рисуем окно и смайлик в нём
    else:
        draw_window(left_bottom, right_top, color, width)  # Рисование окна бей смайла
