from setuptools import setup

#это файл манифест, с полной информацией и завивисмостями в том числе

"""
обязательные параметры
name = <название пакета для распространения (для pip), не должно
пересекатьсяс программным названием>
url = <ссылка для скачивания>
version = <версия> про версии нужно почитать

необязательные параметры
description = <Краткое описание пакета>
author = <имя автора пакета>
author_email = <его email>
license = Лицензия
scripts - запускаемые из командной строки скрипты
packages - необходимые для установки пакеты
py_modules - необходимые для установки модули
install_requires - зависимости
classifiers - тэги
"""
setup(
    name = "mega-math",
    url = "http://github.ubilby.hz",    
    version = "0.0.0",
    description = "Учебный мат модуль",
    author = "ubilby"
    author_email = "ubilby@f.u.yea
    license = "BSD"
    packages = ["mega_math"], #find_packages сам найдет все пакеты
    py_modules = []
    scripts = []
    install_requires = []
    )

#pip - python index package.
#чтобы pip работал с нашим пакетом необходимо зарегестрироваться на pypi.org
#и выслать через pip
#pip может ставить и из гита (из любого портала контроля версий)
#но можно установить и setup.py
