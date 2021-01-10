#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
print('zoo: ', zoo)
# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert( 1, 'bear' )
print('zoo: ', zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
print( 'birds: ', birds )
#  и выведите список на консоль
zoo.extend(birds)
print( 'zoo + birds = ', zoo)

# уберите слона
#  и выведите список на консоль
zoo.remove('elephant')
print( 'zoo: ', zoo )

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
print( 'Лев сидит в клетке №', zoo.index( 'lion' ) + 1 )
print( 'Жаворонок сидит в клетке №', zoo.index( 'lark' ) + 1 )
# зачет!