# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from room_1 import folks as flk1
from room_2 import folks as flk2


print('В комнате room1 живут: ', ', '.join(flk1))
print('В комнате room2 живут: ', ', '.join(flk2))

# зачет!
