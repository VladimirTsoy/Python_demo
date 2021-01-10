# -*- coding: utf-8 -*-

import simple_draw as sd
import copy as cp

sd.resolution = (1300, 600)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длина ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


def draw_branches(point_start, angle0, delta_angle, length_br, width=3, color=sd.COLOR_YELLOW):
    vec_left = sd.get_vector(point_start, angle0 - delta_angle, length_br, width)
    vec_left.draw(color)
    vec_right = sd.get_vector(point_start, angle0 + delta_angle, length_br, width)
    vec_right.draw(color)
    return vec_left, vec_right


def set_next_angle(vector, route_vector, delta_angle):
    """ Устанавливает угол отклонения (медианну) на следующую глубину дерева """
    if vector.end_point.x < vector.start_point.x:
        if vector.angle == 180:
            next_angle = 180 + delta_angle * 0.2
        else:
            next_angle = vector.angle * 1.08

    elif vector.end_point.x > vector.start_point.x:
        if vector.angle == 0:
            next_angle = -delta_angle * 0.2
        else:
            next_angle = vector.angle * 0.92

    else:
        if vector.end_point.y < vector.start_point.y:
            if vector.end_point.x < route_vector.end_point.x:
                next_angle = vector.angle - delta_angle * 0.3
            else:
                next_angle = vector.angle + delta_angle * 0.3

        else:
            next_angle = route_vector.angle

    return next_angle


def draw_branches_recur(lst_vec_start, route, delta_angle, length_br, width=3, color=sd.COLOR_YELLOW):
    if length_br < 10:
        return

    lst_vec_out = []
    for vec in lst_vec_start:
        next_angle = set_next_angle(vec, route, delta_angle)
        left_vec, right_vec = draw_branches(vec.end_point, next_angle, delta_angle, length_br, width, color)
        lst_vec_out.append(left_vec)
        lst_vec_out.append(right_vec)

    next_length = length_br * 0.75
    draw_branches_recur(lst_vec_out, route, delta_angle, next_length, width, color)


# 1. Рисуем дерево в цикле
point_0 = sd.get_point(600, 30)    # Точка откуда будет расти корень
angle = 90                         # Начальный угол для отрисовки корня дерева
delta = 30
length = 90
route_vec = sd.get_vector(point_0, angle, length, 3)  # Корень дерева
route_vec.draw()
routes_vec = [route_vec]       # Векторы на текущем глубине дерева
next_route_vec = []               # Векторы на следующем глубине дерева

while length > 5:
    for limb in routes_vec:
        next_angle = set_next_angle(limb, route_vec, delta)
        left_route_vec, right_route_vec = draw_branches(limb.end_point, next_angle, delta, length)
        next_route_vec.append(left_route_vec)
        next_route_vec.append(right_route_vec)
    routes_vec.clear()
    routes_vec = cp.deepcopy(next_route_vec)  # Сохраняем содержимое next_route_vec для последующей отрисовки
    next_route_vec.clear()
    length *= 0.75

# 2. Рисуем дерево рекурсивно
point_0 = sd.get_point(350, 30)     # Точка откуда будет расти корень
length = 100
width = 2
color = sd.COLOR_GREEN
route = sd.get_vector(point_0, 90, length, width)   # Корень дерева
route.draw(color)
lst_vec = [route]
delta_angle = 30
draw_branches_recur(lst_vec, route, delta_angle, length, width, color)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

# 4. Рисуем со случайными отклонениями
point_0 = sd.get_point(850, 30)     # Точка откуда будет расти корень
angle = 90                  # Начальный угол для отрисовки корня дерева
length = 100
route_vec = sd.get_vector(point_0, angle, length, 3)  # Корень дерева
route_vec.draw()
routes_vec = [route_vec]  # Векторы на текущем глубине дерева
next_route_vec = []          # Векторы на следующем глубине дерева

while length > 5:
    for limb in routes_vec:
        delta = sd.random_number(18, 42)    # рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
        next_angle = set_next_angle(limb, route_vec, delta)
        left_route_vec, right_route_vec = draw_branches(limb.end_point, next_angle, delta, length)
        next_route_vec.append(left_route_vec)
        next_route_vec.append(right_route_vec)
    routes_vec.clear()
    routes_vec = cp.deepcopy(next_route_vec)  # Сохраняем содержимое next_route_vec для последующей отрисовки
    next_route_vec.clear()
    length *= sd.random_number(60, 80) / 100    # рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75

sd.pause()

# зачет!
