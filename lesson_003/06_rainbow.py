# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
sd.resolution = (400, 600)
# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.

A = sd.get_point(50, 50)
B = sd.get_point(350, 450)

for color in rainbow_colors:
    sd.line(A, B, color, 4)
    A.y += 5
    B.y += 5

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

A = sd.get_point(300, -100)
R = 450
step = 10
for color in rainbow_colors:
    sd.circle(A, R, color, step)
    R += step

sd.pause()
# зачет!