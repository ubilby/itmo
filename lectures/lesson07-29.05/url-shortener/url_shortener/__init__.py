import sys #сначала импоттируются встроенные модули, потом скачанные, потом наши 

from url_shortener import storage


#def get_connection():
#    conn = storage.connect("shortener.sqlite") #мы подключаемся к базе (создаем его)

get_connection = lambda: storage.connect("shortener.sqlite") #тоже самое, что и предыдущее создание функции (закоментированное) 



def action_add():
    ok = False

    while not ok:
        url = input("\nВведите URL адрес: ")

        if not url:
            break
    
        if url.startswith(("http://", "https://", "ftp://", "ftps://",)): #демонстрация работы метода statrswith
            with get_connection() as conn:
                sort_url = storage.add_url(conn, url)
            print("Короткий адрес: {}".format(sort_url))
            ok = True

        else:
            print("Не корректный url-адрес")

            
def action_find():
    short_url = input("\nВведите короткий URLадрес")
    if short_url:
        with get_connection() as conn:
            url = storage.find_url_by_short(conn, short_url)

        if url:
            url = url.get("original_url")
            print("Оригинальный URL-адрес: {}".format(url))
        else:
            print("Оригинальный адрес не найден")
            


def action_find_all():
    with get_connection() as conn:
        urls = storage.find_all(conn)

    for url in urls: #демонстрация работы format
        print("{url[short_url]} - {url[original_url]} - {url[created]}".format(url=url))


def action_show_menu(): #само меню. все форматирование, добавленное в тройных кавычках сохранится и в результате дйствия фнукции принт
    """обработчик действия показать меню"""
    print('''
URL Shotener v1.0
1. Добавиьть адрес
2. Найти оригинальный URL-адрес
3. Вывести все URL-адреса
m. Показать меню
q. Выйти
''')
    pass


def action_exit():
    """Обработчик Действия выйти"""
    sys.exit(0) #если код - ноль, по стандарту - все ок


def main():
    with get_connection() as conn:
        storage.initialize(conn)

    action_show_menu()

    actions = {
            "1" : action_add,
            "2" : action_find,
            "3" : action_find_all,
            "m" : action_show_menu,
            "q" : action_exit
            }    

    while 1:
        action_show_menu()
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd) #если пользователь введт не из словаря значение, .get вернет None

        if action:
            action()
        else:
            print("Неизвестная команда")

#если в модуле много функций, но некоторые из них объединены какоим-то смыслом, то по ПЕП удобно делать общий префикс в названии
