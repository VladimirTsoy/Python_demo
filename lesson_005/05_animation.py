import results.draw_image.rainbow as rb
import results.draw_image.wall as wl
import results.draw_image.smile as sm
import results.draw_image.tree as tr
import results.draw_image.snow as sn
import results.draw_image.sun as sun
import results.draw_image.human as human
import simple_draw as sd

sd.resolution = (1300, 900)

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

# ******** С анимацией *********

# ================ Дом ================= #
wl.draw_house(20, 15, sd.get_point(400, 250), smile=0)

# ================ Дерево ================= #
tr.draw_tree(sd.get_point(970, 270), 90, 30, 90, sd.COLOR_DARK_YELLOW, 2)

# ================ Солнце ================= #
sun.draw_sun(sd.get_point(150, 760), 50, sd.COLOR_YELLOW, 2)

# ================ Человек ================= #
human.draw_human(sd.get_point(650, 300), 70)

# Инициализируем параметры радуги
start_rainbow = sd.get_point(400, 100)  # Точка начала радуги
radius_rainbow = 1000  # Радиус радуги
step_rainbow = 20
lst_color = list(rb.rainbow_colors)

# Инициализируем параметры солнца
center_sun = sd.get_point(150, 760)
radius_sun = 50
delta_angle_sun = 30
start_angle_sun = 0

# Инициализируем параметры снежинок
h0_snowdrift = 300  # Начальная высота, на которой будет накапливаться снег
left_bottom_snow = sd.get_point(100, 250)
right_top_snow = sd.get_point(300, 500)
snowflake_param, delta_x, delta_y = sn.init_snow(left_bottom_snow, right_top_snow, 20)


while True:
    sd.start_drawing()

    rb.flash_rainbow(start_rainbow, radius_rainbow, step_rainbow, lst_color)
    start_angle_sun = sun.shimmers_sun(center_sun, radius_sun, start_angle_sun, delta_angle_sun)
    sm.flashing_smiley(485, 340, 25)
    h0_snowdrift = sn.snowfall(left_bottom_snow, right_top_snow, snowflake_param, delta_x, delta_y, h0_snowdrift)
    sd.finish_drawing()

    sd.sleep(1)

    if sd.user_want_exit() or h0_snowdrift > right_top_snow.y:
        break

sd.pause()

# зачет!
