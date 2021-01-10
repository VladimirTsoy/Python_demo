import simple_draw as sd
import copy as cp


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


def draw_branches(point_start, angle0, delta_angle, length_br, width=3, color=sd.COLOR_YELLOW):
    vec_left = sd.get_vector(point_start, angle0 - delta_angle, length_br, width)
    vec_left.draw(color)
    vec_right = sd.get_vector(point_start, angle0 + delta_angle, length_br, width)
    vec_right.draw(color)
    return vec_left, vec_right


def draw_tree_random(point_0, angle, length, color=sd.COLOR_YELLOW, width=1):
    route_vec = sd.get_vector(point_0, angle, length, width)  # Корень дерева
    route_vec.draw(color)
    routes_vec = [route_vec]  # Векторы на текущем глубине дерева
    next_route_vec = []  # Векторы на следующем глубине дерева

    while length > 5:
        for limb in routes_vec:
            delta = sd.random_number(18, 42)  # рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
            next_angle = set_next_angle(limb, route_vec, delta)
            left_route_vec, right_route_vec = draw_branches(limb.end_point, next_angle, delta, length, width, color)
            next_route_vec.append(left_route_vec)
            next_route_vec.append(right_route_vec)
        routes_vec.clear()
        routes_vec = cp.deepcopy(next_route_vec)  # Сохраняем содержимое next_route_vec для последующей отрисовки
        next_route_vec.clear()
        length *= sd.random_number(60, 80) / 100  # Отклонение длины ветвей в пределах 20% от коэффициента 0.75

    for limb in routes_vec:  # Закрасим кончики в зелёный цвет
        limb.draw(sd.COLOR_GREEN)


def draw_tree(point_0, angle, delta, length, color=sd.COLOR_YELLOW, width=1):
    sd.start_drawing()
    route_vec = sd.get_vector(point_0, angle, length, width)  # Корень дерева
    route_vec.draw(color)
    routes_vec = [route_vec]  # Векторы на текущем глубине дерева
    next_route_vec = []  # Векторы на следующем глубине дерева

    while length > 5:
        for limb in routes_vec:
            next_angle = set_next_angle(limb, route_vec, delta)
            left_route_vec, right_route_vec = draw_branches(limb.end_point, next_angle, delta, length, width, color)
            next_route_vec.append(left_route_vec)
            next_route_vec.append(right_route_vec)
        routes_vec.clear()
        routes_vec = cp.deepcopy(next_route_vec)  # Сохраняем содержимое next_route_vec для последующей отрисовки
        next_route_vec.clear()
        length *= 0.75

    for limb in routes_vec:  # Закрасим кончики в зелёный цвет
        limb.draw(sd.COLOR_GREEN)

    sd.finish_drawing()
