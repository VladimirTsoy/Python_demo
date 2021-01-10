# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 600)
# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

#    Инициализируем словарь цветов
colors = {1: ['красный', sd.COLOR_RED],    2: ['оранжевый', sd.COLOR_ORANGE],   3: ['желтый', sd.COLOR_YELLOW],
          4: ['зелёный', sd.COLOR_GREEN],  5: ['морская волна', sd.COLOR_CYAN], 6: ['синий', sd.COLOR_BLUE],
          7: ['розовый', sd.COLOR_PURPLE], 8: ['черный', sd.COLOR_BLACK],       9: ['белый', sd.COLOR_WHITE]}


def triangle(point0_, length_, angle_=0, width_=1, color_=sd.COLOR_YELLOW):
    """Функция рисования треугольника"""""

    tmp_point = point0_
    for angle_next in range(0, 241, 120):
        v = sd.get_vector(tmp_point, angle_ + angle_next, length_, width_)
        v.draw(color_)
        sd.line(tmp_point, v.start_point, color_, width_)
        tmp_point = v.end_point
    sd.line(point0_, tmp_point, color_, width_)


def foursquare(point0_, length_, angle_=0, width_=1, color_=sd.COLOR_YELLOW):
    """Функция рисования квадрата"""""

    tmp_point = point0_
    for angle_next in range(0, 271, 90):
        v = sd.get_vector(tmp_point, angle_ + angle_next, length_, width_)
        v.draw(color_)
        sd.line(tmp_point, v.start_point, color_, width_)
        tmp_point = v.end_point
    sd.line(point0_, tmp_point, color_, width_)


def pentagon(point0_, length_, angle_=0, width_=1, color_=sd.COLOR_YELLOW):
    """Функция рисования пятиугольника"""""

    tmp_point = point0_
    for angle_next in range(0, 289, 72):
        v = sd.get_vector(tmp_point, angle_ + angle_next, length_, width_)
        v.draw(color_)
        sd.line(tmp_point, v.start_point, color_, width_)
        tmp_point = v.end_point
    sd.line(point0_, tmp_point, color_, width_)


def hexagon(point0_, length_, angle_=0, width_=1, color_=sd.COLOR_YELLOW):
    """Функция рисования шестиугольника"""""

    tmp_point = point0_
    for angle_next in range(0, 301, 60):
        v = sd.get_vector(tmp_point, angle_ + angle_next, length_, width_)
        v.draw(color_)
        sd.line(tmp_point, v.start_point, color_, width_)
        tmp_point = v.end_point
    sd.line(point0_, tmp_point, color_, width_)


def draw_shapes(color_shape):
    length_triangle = 200
    point_triangle = sd.get_point(200, 200)
    angle_triangle = 0
    triangle(point_triangle, length_triangle, angle_triangle, 4, color_shape)

    length_foursquare = 100
    point_foursquare = sd.get_point(500, 200)
    angle_foursquare = 30
    foursquare(point_foursquare, length_foursquare, angle_foursquare, 4, color_shape)

    length_pentagon = 100
    point_pentagon = sd.get_point(800, 200)
    angle_pentagon = 90
    pentagon(point_pentagon, length_pentagon, angle_pentagon, 4, color_shape)

    length_hexagon = 100
    point_hexagon = sd.get_point(500, 400)
    angle_hexagon = 90
    hexagon(point_hexagon, length_hexagon, angle_hexagon, 4, color_shape)


while True:
    for color in colors:
        print(color, ' - ', colors[color][0])

    user_input = input('Введите цвет из заданного списка:')

    if not user_input.isdigit():
        print('Номер должен быть числом. Попробуйте еще раз. \n')
        continue

    user_input = int(user_input)

    if user_input in colors:
        color = colors[user_input][1]
        draw_shapes(color)
        break
    else:
        print('Вы ввели неверный номер. Поробуйте еще раз. \n')

sd.pause()

# зачет!
