# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

len_brick, height_brick = 100, 50
n, m = 10, 12  # Количество кирпичиков в длину и высоту соотв.
sd.resolution = (n * len_brick, m * height_brick)
left_bottom = sd.get_point(-len_brick, 0)  # Левая нижняя точка прямоугльника
right_top = sd.get_point(0, height_brick)  # Правая верхняя точка
shift = len_brick / 2.0

for i in range(1, m + 1):
    for j in range(n + 2):  # Рисуем по одному лишнему кирпичу слева и справа
        sd.rectangle(left_bottom, right_top, sd.COLOR_YELLOW, 1)
        left_bottom.x += len_brick
        right_top.x += len_brick
    left_bottom.y += height_brick
    right_top.y += height_brick
    if i % 2:
        left_bottom.x = -len_brick + shift
        right_top.x = shift
    else:
        left_bottom.x = -len_brick
        right_top.x = 0

# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

sd.pause()
# зачет!