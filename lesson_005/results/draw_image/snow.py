import simple_draw as sd


def init_snow(left_bottom, right_top, length_snow, n=50):
    """ Инициализация начальных параметров снежинок """

    snowflake_param = []
    delta_y = (right_top.y - left_bottom.y) * 0.1
    delta_x = (right_top.x - left_bottom.x) * 0.07
    for _ in range(n):          # Инициализируем начальные параметры снежинок
        x = sd.random_number(left_bottom.x, right_top.x)
        y = sd.random_number(right_top.y - right_top.y * 0.1, right_top.y)
        length_snow_rand = sd.random_number(length_snow - length_snow * 0.1, length_snow + length_snow * 0.1)
        snowflake_param.append([x, y, length_snow_rand])

    return snowflake_param, delta_x, delta_y


def ret_2nd_ele(some_list):
    return some_list[1]


# find Min from a list of tuples with key on the basis of the 2nd element
# print("Min in list of tuples : ", min(list_of_tuples, key=ret_2nd_ele))
# print('min of snowflake_param = ', min(snowflake_param, key=ret_2nd_ele))

def draw_snowdrift(left_bottom, right_top, length, color=sd.COLOR_WHITE, n=50):
    """ Рисование сугроба. heigth0 - высота, на котором будет сугроб
        n - количество снежинок """

    for _ in range(n):
        x = sd.random_number(left_bottom.x, right_top.x)
        y = sd.random_number(left_bottom.y, right_top.y)
        sd.snowflake(sd.get_point(x, y), length, color)


def draw_snowflake(x_, y_, length_, color_=sd.COLOR_WHITE):
    point_snow = sd.get_point(x_, y_)
    sd.snowflake(point_snow, length_, color_)


def snowfall(left_bottom, right_top, snowflake_param, delta_x, delta_y, h0_snowdrift, n=15, delta_snowdrift=2):
    """ Рисование снегопада.  snowflake_param - начальные параметры снежиноок,
    h0_snowdrift - Начальная высота, на которой будет накапливаться снег,
    delta_snowdrift - высота слоя выпадения снега"""

    for i in range(n):
        # Достаём параметры снежинки и печатаем её цветом фона
        x = snowflake_param[i][0]
        y = snowflake_param[i][1]
        length = snowflake_param[i][2]
        draw_snowflake(x, y, length, sd.background_color)

        # Изменяем координаты снежинки и рисуем её белым цветом
        x += sd.random_number(int(-delta_x), int(delta_x))
        y -= delta_y
        draw_snowflake(x, y, length)

        if y < h0_snowdrift:
            x = sd.random_number(int(left_bottom.x), int(right_top.x))
            y = sd.random_number(int(right_top.y - delta_y), int(right_top.y + delta_y))

        snowflake_param[i] = [x, y, length]

    if min(snowflake_param, key=ret_2nd_ele)[1] <= h0_snowdrift:
        h0_snowdrift += delta_snowdrift

    return h0_snowdrift
