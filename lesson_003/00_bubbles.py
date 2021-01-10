# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
center = sd.get_point(600, 300)
radius = 100

sd.circle(center, radius, sd.COLOR_RED, 2)

radius += 5
sd.circle(center, radius, sd.COLOR_RED, 2)

radius += 5
sd.circle(center, radius, sd.COLOR_RED, 2)


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def draw_buble(center_pos, radius, step, color, width_pen=1):
    """ 
        This function for draw buble
    """
    sd.circle(center_pos, radius, color, width_pen)

    radius += step
    sd.circle(center_pos, radius, color, width_pen)

    radius += step
    sd.circle(center_pos, radius, color, width_pen)


center, radius = sd.get_point(300, 250), 50
draw_buble(center, radius, 7, sd.COLOR_DARK_CYAN, 2)

# Нарисовать 10 пузырьков в ряд
center, radius = sd.get_point(150, 400), 60
center.x += 5
print('x = ', center.x, ' y = ', center.y)
for _ in range(10):
    draw_buble(center, radius, 7, sd.COLOR_DARK_CYAN, 2)
    center.x += 100
    print('center.x = ', center.x)

# Нарисовать три ряда по 10 пузырьков
x0, y0 = 100, 50
center, radius = sd.get_point(x0, y0), 30
for y in range(y0, 160, 30):
    for x in range(x0, 900, 80):
        draw_buble(center, radius, 5, sd.COLOR_DARK_PURPLE, 2)
        center.x = x
    center.y = y

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
radius = 27
for _ in range(100):
    center = sd.random_point()
    draw_buble(center, radius, 3, sd.random_color())

sd.pause()

# зачет!
