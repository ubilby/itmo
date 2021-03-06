"""тремя двойным кавычками документируется модуль(файл) вначале (перед этим комментарием может быть только комментарий скодировкой и запускаемые знаки для мака и линукса?!"""

#Модули и пакеты

#Модули

#Python ищет модули по следубщей схеме:
    #сначала в текущей папки, затем в python_path


import sys #стандартный модуль

print(sys.path) #собсна python path



#существуют разные типы импорта:
#указание модуля целиком (все пространство имен). import <название модуля>
import square_shapes

#чатстичный импорт. from <название модуля> import <имя функции>
from square_shapes import calculate_square_area

#чатстичный импорт. с переименованием from <название модуля> import <имя функции> as <новое имя функции>
from square_shapes import calculate_square_area as fu

#полный импорт с переименованием модуля
import os.path as Path #стандартный модуль
import square_shapes as ss

#импортировать имена из модуля в текущее пространства имен
from square_shapes import * #звездочка - это плохо, или зло))



#питон контролирует запуск модулей и два раза запустить не получится (сомнительно, но допустим)
#питон скомпилировал библиотеку в __pycache__ в третьем питоне, при изменении библиотека перекомпилуруется (в файл *.pyc)
#во втором питоне создавался одноименный файл с другим расширением (*.pyc)
#пики могу закэшироваться и создать проблемм (в редких слуаях)
#если запустить "python3 -O имя_файла" то создастся *.pyc со всеми библиотеками, и на другом копьютере можно будет запустить
#сам этот файл main.py можно будет ипмортировать

#не рекомендуется называть файлы и функции  начиная с двойных подчеркиваний

#все что в теле условия (см. следующий кусок кода) -  выполнится, только если файл будет испускаемым, но не имортируемым
    #это может пригодиться, для, например, тестов
print(__name__)
if __name__ == "__main__":
    print(
        square_shapes.calculate_square_area(4),
        calculate_square_area(5),
        fu(6),
        Path.basename(__doc__),
        sep = "\n"
        )

print(dir(square_shapes)) #dir перечисляет все пространство имен


#пакеты

#в третьем питоне любая папка - может быть пакетом, во втором питоне директория - пакет, если есть файл __init__.py продолжение в main.py
