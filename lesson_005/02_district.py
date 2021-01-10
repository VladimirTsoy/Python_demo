# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from central_street.house1 import room1 as flk1
from central_street.house1 import room2 as flk2
from central_street.house2 import room1 as flk3
from central_street.house2 import room2 as flk4

from soviet_street.house1 import room1 as flk5
from soviet_street.house1 import room2 as flk6
from soviet_street.house2 import room1 as flk7
from soviet_street.house2 import room2 as flk8

gen_folks = flk1.folks + flk2.folks + flk3.folks + flk4.folks + flk5.folks + flk6.folks + flk7.folks + flk8.folks

print('На районе живут: \n', '\n '.join(gen_folks))

# зачет!
