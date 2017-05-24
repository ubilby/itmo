

import mega_math # импортировать весь пакет (возможно только при прописанных импортахв в файле __init__.py

mega_math.square_shapes.calculate_square_area(5)

import mega_math.square_shapes as ss #импортировать функцию из модуля из пакета и именовать
print(ss.calculate_rechtangle_area(7, 8))

from mega_math import square_shapes #импортировать модуль из пакета
print(square_shapes.calculate_rechtangle_area(9, 5))


from mega_math.square_shapes import calculate_square_area #импортировать функцию из модуля из пакета
print(calculate_square_area(7))

#создавая пакет, необходимо в __init__.py импортировать все модули
#допустим, я хочу распространить модуль и/или пакет: делается это с помощью файла setup.py
#в setup.py должна быть вся инфа о создании см. файл setup.py 
#
