# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def triangle(point0_, length_, angle_=0, width_=1):
    """Функция рисования треугольника"""

    tmp_point = point0_
    for angle_next in range(0, 241, 120):
        v = sd.get_vector(tmp_point, angle_ + angle_next, length_, width_)
        v.draw()
        sd.line(tmp_point, v.start_point, width=width_)
        tmp_point = v.end_point
    sd.line(point0_, tmp_point, width=width_)


def foursquare(point0_, length_, angle_=0, width_=1):
    """Функция рисования квадрата"""

    tmp_point = point0_
    for angle_next in range(0, 271, 90):
        v = sd.get_vector(tmp_point, angle_ + angle_next, length_, width_)
        v.draw()
        sd.line(tmp_point, v.start_point, width=width_)
        tmp_point = v.end_point
    sd.line(point0_, tmp_point, width=width_)


def pentagon(point0_, length_, angle_=0, width_=1):
    """Функция рисования пятиугольника"""

    tmp_point = point0_
    for angle_next in range(0, 289, 72):
        v = sd.get_vector(tmp_point, angle_ + angle_next, length_, width_)
        v.draw()
        sd.line(tmp_point, v.start_point, width=width_)
        tmp_point = v.end_point
    sd.line(point0_, tmp_point, width=width_)


def hexagon(point0_, length_, angle_=0, width_=1):
    """Функция рисования шестиугольника"""

    tmp_point = point0_
    for angle_next in range(0, 301, 60):
        v = sd.get_vector(tmp_point, angle_ + angle_next, length_, width_)
        v.draw()
        sd.line(tmp_point, v.start_point, width=width_)
        tmp_point = v.end_point
    sd.line(point0_, tmp_point, width=width_)


length_triangle = 100
point_triangle0 = sd.get_point(100, 50)
angle_triangle = 30
triangle(point_triangle0, length_triangle, angle_triangle, 4)


length_foursquare = 100
point_foursquare0 = sd.get_point(250, 50)
angle_foursquare = 0
foursquare(point_foursquare0, length_foursquare, angle_foursquare, 4)


length_pentagon = 100
point_pentagon0 = sd.get_point(500, 50)
angle_pentagon = 30
pentagon(point_pentagon0, length_pentagon, angle_pentagon, 4)


length_hexagon = 100
point_hexagon0 = sd.get_point(850, 70)
angle_hexagon = 90
hexagon(point_hexagon0, length_hexagon, angle_hexagon, 4)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


def gen_draw_shapes(point_start, length_shape, angle_start, num_corners, delta_corner, width_=2):

    tmp_point = point_start     # Точка начала отрисовки
    gen_sum_angle = num_corners * delta_corner + 1  # Сумма всех углов + 1
    color_shapes = sd.COLOR_WHITE
    for angle_next in range(0, gen_sum_angle, delta_corner):
        vec = sd.get_vector(tmp_point, angle_start + angle_next, length_shape, width_)
        vec.draw(color_shapes)
        sd.line(tmp_point, vec.start_point, color_shapes, width_)
        tmp_point = vec.end_point
    sd.line(point_start, tmp_point, color_shapes, width_)


def triangle_gen(point0_, length_, angle_=0, width_=1):
    """Функция рисования треугольника c общей функцией"""

    gen_draw_shapes(point0_, length_, angle_, 2, 120, width_)


def foursquare_gen(point0_, length_, angle_=0, width_=1):
    """Функция рисования квадрата c общей функцией"""

    gen_draw_shapes(point0_, length_, angle_, 3, 90, width_)


def pentagon_gen(point0_, length_, angle_=0, width_=1):
    """Функция рисования пятиугольника c общей функцией"""

    gen_draw_shapes(point0_, length_, angle_, 4, 72, width_)


def hexagon_gen(point0_, length_, angle_=0, width_=1):
    """Функция рисования шестиугольника c общей функцией"""

    gen_draw_shapes(point0_, length_, angle_, 5, 60, width_)


length_triangle = 100
point_triangle0 = sd.get_point(150, 350)
angle_triangle = 30
triangle_gen(point_triangle0, length_triangle, angle_triangle, 4)


length_foursquare = 100
point_foursquare0 = sd.get_point(350, 350)
angle_foursquare = 0
foursquare_gen(point_foursquare0, length_foursquare, angle_foursquare, 4)


length_pentagon = 100
point_pentagon0 = sd.get_point(600, 350)
angle_pentagon = 30
pentagon_gen(point_pentagon0, length_pentagon, angle_pentagon, 4)


length_hexagon = 100
point_hexagon0 = sd.get_point(900, 350)
angle_hexagon = 90
hexagon_gen(point_hexagon0, length_hexagon, angle_hexagon, 4)

sd.pause()

# зачет!
