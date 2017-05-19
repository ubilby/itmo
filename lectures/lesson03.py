# условный оператор
print("условный оператор")

a = 10
b = 20

if a < b:
    #pass - пустой блок кода
    print("a < b")
elif a == b:    #необязательный блок
    print("a = b")
else:   #необязательный блок, говорят, что это зло =)
    print("a >= b")

uid = None  #взяли из вне

if uid is None:
    uid = 1
else:
    uid = uid


#тернарный оператор
uid = uid if uid is not None else 1
print(1) if a < b else print(2)

# циклы
# цикл while
print()
print("цикл while")
i=0
while i < 10: #условие цикла
    
    #далее тело цикла
    if i % 2: # тоже самое что и if i %2 = True
        i += 1
        print(i)
        continue #  - continue считается злом! пропустить остаток тела цикла
        print(i)
    i += 1
    
i=0
while True: #бесконечный цикл
    if i > 10:
        break # break - выход из цикла
    i += 1


# and - логическое И
# or - логическое ИЛИ

print()
#цикл for
print("цикл for")
for i in [1, 2, 3, 4, 5]:
    print(i)

print()
print(" методы словаря")

dict1 = {
        "id" : 1,
        "fio" : "Иван Иваныч",
        "is_developer" : True
        }

for i in dict1:
    print(i, dict1[i])


#методы словаря
for i, j in dict1.items(): # items перебирает keys, values
    print(i, j) #распаковка кортежа, если оставить одну переменную,
                #то цикл будет возвращать кортежи

for i in dict1.keys(): # keys перебирает ключи
    print(i)

for i in dict1.values(): # values перебирает значения
    print(i)

keys = ["id","fio","is_developer"]
values = [2, "Петр Петрович", False]
print(dict(zip(keys, values))) #приводят два списка к словарю если заменить
                               #dict на list, то будет список кортежей

#len - возвращает количество переменных в контейнере(списки,
#кортеже, строке, словаре)
skills = dict1["skills"] if "skills" in dict1 else []
print("check")
print(dict1.get("skills")) # вернет значение по ключу, и None если такого ключа нет
skills = dict1["skills"] if "skills" in dict1 else []
dict1["skills"] = None
print(dict1.get("skills", []))
print("check")


lst = (1, 2, 2, 2, 3, 1, 3)
print(lst.count(2)) #счетчик, в данном случае двойки
print()


#слайсинг
s1 = "I love Python!"
print(s1[0], type(s1[0])) #первый элемент
print(s1[::-1]) #строка в обратном порядке
print(s1[::2]) #строка с шагом в 2
print(s1[:5]) #с нулевого по пятый
print(s1[4:]) # с четвертого до конца


print()

#списки

#list.append(a) - добавление a в конец списка
#list.insert(i, a) - добавление a в позицию i (или в конец, если такой позиции нет), список увеличится
#list.remove(a) # удалить первое вхождение a из списка
#list.index(a) - получение индекса первого вхождения a
#del a - удаляет переменную а
lst1 = [1, 2, 3, 4]
lst2 = lst1
lst2.append(5)
print(lst1)
print(lst2)
