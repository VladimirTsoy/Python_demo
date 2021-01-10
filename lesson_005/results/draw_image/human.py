import simple_draw as sd
from lesson_005.results.draw_image import smile


def draw_human(point, length_body, color=sd.COLOR_YELLOW, width=1, factor_a=20, factor_b=30):
    """ Функция рисования человека. factor_a - расположения ног,
        factor_b - расположение рук """

    body = sd.get_vector(point, 90, length_body, width)
    body.draw(color)  # Отрисовка тела

    #               Отрисовка ног
    left_foot = sd.get_vector(point, 270 - factor_a, length_body, width)
    right_foot = sd.get_vector(point, 270 + factor_a, length_body, width)
    left_foot.draw(color)
    right_foot.draw(color)

    #               Отрисовка рук
    hand_point = sd.get_point(point.x, point.y + 2.0 * length_body / 3.0)     # Точка из которой растут руки
    left_hand = sd.get_vector(hand_point, 270 - factor_b, 2.0 * length_body / 3.0, width)
    right_hand = sd.get_vector(hand_point, 270 + factor_b, 2.0 * length_body / 3.0, width)
    left_hand.draw(color)
    right_hand.draw(color)

    #               Отрисовка головы
    radius_had = length_body / 3.0
    smile.draw_smile(point.x, body.end_point.y + radius_had, radius_had, color)


# def flashing_human(point, length_body, color=sd.COLOR_YELLOW, width=1, factor_a=20, factor_b=30):
#     num = sd.random_number(0, 1)
#     if num == 0:
#         smile_blink(x, y, radius, sd.background_color, width)
#         draw_human(point, length_body, color, width, factor_a, factor_b)
#     else:
#         draw_smile(x, y, radius, sd.background_color, width)
#         smile_blink(x, y, radius, color, width)