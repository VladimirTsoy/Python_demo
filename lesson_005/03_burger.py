# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

import my_burger as mb

print('Рецепт двойного чизбургера:')
print('Перед готовкой тщательно вымойте руки и подготовте необходимые ингридиенты!')
mb.add_loaf()
mb.add_rissole()
mb.add_cheese()
mb.add_rissole()
mb.add_cheese()
mb.add_cucumber()
mb.add_tomato()
mb.add_onion()
mb.add_mayo()
mb.add_mustard()
mb.add_ketchup()
mb.add_loaf()

# зачет!
