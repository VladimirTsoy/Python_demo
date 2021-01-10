# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


# Инициализируем словарь цветов
colors = {1: ['красный', sd.COLOR_RED], 2: ['оранжевый', sd.COLOR_ORANGE], 3: ['желтый', sd.COLOR_YELLOW],
          4: ['зелёный', sd.COLOR_GREEN], 5: ['морская волна', sd.COLOR_CYAN], 6: ['синий', sd.COLOR_BLUE],
          7: ['розовый', sd.COLOR_PURPLE], 8: ['черный', sd.COLOR_BLACK], 9: ['белый', sd.COLOR_WHITE]}


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


# Инициализируем словарь фигур
shapes = {1: ['треугольник', triangle],  2: ['квадрат', foursquare],
          3: ['пятиугольник', pentagon], 4: ['шестиугольник', hexagon]}

# Параметры фигур
length = 200
point0 = sd.get_point(500, 200)
angle = 0

# тут добавим новую переменную
color_draw = None

while True:
    for color in colors:
        print(color, ' - ', colors[color][0])

    input_color = input('Введите цвет из заданного списка:')
    if not input_color.isdigit():
        print('Номер должен быть числом. Попробуйте еще раз. \n')
        continue

    input_color = int(input_color)

    if input_color in colors:
        # тут будем использовать color_draw а не просто color
        color_draw = colors[input_color][1]
        break
    else:
        print('Вы ввели неверный номер. Поробуйте еще раз. \n')


while True:
    for num_shape in shapes:
        print(num_shape, ' - ', shapes[num_shape][0])

    input_shape = input('Введите номер фигуры: ')
    if not input_shape.isdigit():
        print('Номер должен быть числом. Попробуйте еще раз. \n')
        continue

    input_shape = int(input_shape)

    if input_shape in shapes:
        # и тут мы будем использовать color_draw за место color, потому что у вас сейчас color подсвечивалось как не
        # как не определена
        shapes[input_shape][1](point0, length, angle, 2, color_draw)
        break

    else:
        print('Вы ввели неверный номер. Поробуйте еще раз. \n')


sd.pause()

# зачет!
