
#Функции и области видимости переменных

def say_hello():    #def оператор объявления функции
    print("Hello, Python!")
    
say_hello() # вызов функции

#аргументы функции
def say_hello_2(name):
    print("hello,", name)

say_hello_2("Вася")
say_hello_2("Петя")

def summa(a, b):
    print("Сумма:", a+b)

summa(1, 2)

#Как вернуть значкние из функции?
def mega_pow(x, p):
    return x**p
    
c = mega_pow(2, 8)
print(c)
print(mega_pow(3, 5))

def connect(kosta, user, passwwd, baname):
    if dn_connect(kosta, server, passwd):
        if db_set(dbname):
            print("Работаем!")
        else:
            print("Нет такой ДБ")
    else:
        if not dn_connect(kosta, server, passwd):
            print("Нет такого соединения")
            return False
    print("Работаем")
    return True

mega_pow(mega_pow(5, 8), 2)

#как избавиться от  elif???

#Значения аргументов по-умолчанию:
def extra_pow(x, p=2):
    """Эта функция возводит в
    степень (второго аргумента, по-умолчанию = 4) первый аргумент"""
    return x ** p
print("Extra pow: ", extra_pow(2))
print("Extra pow: ", extra_pow(2,3))


#Передача аргументов по ссылке

def parse(src, output):
    src = src.strip(".") # strip() - удалит символы с начала и конца строки

    for i in src.split(): # split() - разбивает строку по указонному симфолу, по-умолчанию - пробел
        output.append(i)

src = "Python is a programming language."
lst = []

parse(src, lst)
print(src, lst)


#переменное количество аргументов

def multi(*args): #здесь args - список аргументов
    result = 1
    for i in args:
        result *= i
    return result

print(multi(1, 2, 3, 4, 5))
lst2 = [1, 2, 3, 4, 5]
print(multi(*lst2))

# позиционные и именованные аргументы

def join1(i, separator="", lst=None):
    if lst is None:
        lst = []

    return separator.join(lst)

print(join1(5, lst = ["a", "b", "c"], separator = "!"))


def make_query_string(separator="&", **kwargs): #kwargs - здесь словарь
    l = []
    for name, value in kwargs.items():
#        l.append(name + "+" + value)
        l.append("{}={}".format(name,value))
    return separator.join(l)

print(make_query_string(uid = "1", fio = "Mamev", ))

d = {
    "separator" : "..!.",
    "id" : 1,
    "name" : "Neo"
    }
print(make_query_string(**d))


#анонимная функция (лямбда функция)
def sqrt(x):
    return x **0.5

sqrtlam = lambda x : x**0.5

print(sqrtlam(9))


#замыкание
def wrapper():
    print()
    
    def do_something():
        pass

    print()

def trim(chars = None):
    return lambda s : s.strip(chars)

spaces_trim = trim(" ") #функция каррирования или частичное применение
slashes_trim = trim ("/\\")

#рекурсивная функция
def factorial(x):
    
    return 1 if x == 0 else x * factorial(x-1)

print("факториал: {}".format(factorial(8)))


#прмиер косвенной рекурсии!!!
"""def a():
    b()
def b():
    a()"""
#ЗАПРЕЩЕННО!!!!

#область видимости и время жизни переменных
"""
1) Глобальная область видимости.
    - все кроме функций и классов
    глобальные переменные живут, пока выполняется программа
    - globals()
        'var' in globals()? - вернет Тру или Фолс?
2) Локальная область видимости.
    - функции и классы
    локальные переменные живут пока живут функции (не (за исключением замыканий)
        'var' in locals() - вернет внутри функции, вернет Тру или Фолс
"""
g = 666

def wrapper2():
    
    external = 777
    
    def func():
        global g #глобализирует g - Глобальные переменные - ЗЛО!!!
        nonlocal external #для случаев, когда переменная локальная
        #для предыдущей функции (и берется из ее области видимости)
        #ТОЛЬКО ТРЕТИЙ ПИТОН!
        g += 1
        external += 1
        print(g, external)
        
    func()
    
wrapper2()
