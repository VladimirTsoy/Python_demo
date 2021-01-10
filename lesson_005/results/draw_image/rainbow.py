import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def direct_rainbow(point_start, point_end, width=4):
    for color in rainbow_colors:
        sd.line(point_start, point_end, color, width)
        point_start.y += 5
        point_end.y += 5


def curve_rainbow(point_start, radius, step=10):
    for color in rainbow_colors:
        sd.circle(point_start, radius, color, step)
        radius += step


def curve_rainbow_wink(point_start, radius, step=10):
    for color in rainbow_colors:
        sd.circle(point_start, radius, color, step)
        sd.sleep(0.2)
        radius += step


def hide_curve_rainbow(point_start, radius, step=10, color=sd.background_color):
    for _ in range(7):
        sd.circle(point_start, radius, color, step)
        sd.sleep(0.2)
        radius += step


def flash_rainbow(center_point, radius_start, step, lst_color):
    tmp_radius = radius_start
    for color in lst_color:
        sd.circle(center_point, radius_start, color, step)
        radius_start += step

        if radius_start > tmp_radius + 6 * step:
            radius_start = tmp_radius
            tmp_color = lst_color[-1]
            lst_color.pop()
            lst_color.insert(0, tmp_color)

