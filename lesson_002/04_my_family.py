#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Отец: Леонид', 'Мама: Каролина', 'Брат: Александр', 'Брат: Дмитрий', 'Дедушка: Афанасий']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Леонид', 165],
    ['Каролина', 160],
    ['Александр', 170],
    ['Дмитрий', 110],
    ['Афанасий', 160]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

print('Рост отца - ', my_family_height[0][1], ' см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
tmp = 0

for i in range( len(my_family_height) ):
    tmp += my_family_height[i][1]

print('Общий рост моей семьи - ', tmp, ' см')
# зачет!