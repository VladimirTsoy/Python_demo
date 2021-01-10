#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint as pp
# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}
print('Города: ', sites, '\n')

        # Москва
Moscow_to_London =  ( ( sites['Moscow'][0] - sites['London'][0] )**2 + ( sites['Moscow'][1] - sites['London'][1] )**2 )**0.5
Moscow_to_Paris =  ( ( sites['Moscow'][0] - sites['Paris'][0] )**2 + ( sites['Moscow'][1] - sites['Paris'][1] )**2 )**0.5
distances['Moscow'] = {}
distances['Moscow']['London'] = Moscow_to_London
distances['Moscow']['Paris']  = Moscow_to_Paris

        # Лондон
London_to_Paris = ( ( sites['London'][0] - sites['Paris'][0] )**2 + ( sites['London'][1] - sites['Paris'][1] )**2 )**0.5
distances['London'] = {}
distances['London']['Moscow'] = Moscow_to_London
distances['London']['Paris']  = London_to_Paris

        # Париж
distances['Paris'] = {}
distances['Paris']['Moscow'] = Moscow_to_Paris
distances['Paris']['London'] = London_to_Paris

print('\t\t\t Расстояния: ')
pp( distances )
# зачет!



