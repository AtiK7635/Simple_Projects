# == Калькулятор корней ==#

# a, b, c = map(int, input("Введите 3 числа").split())
# result = b ** 2 - 4 * a * c
# x1 = (-b + result ** 0.5) / (2 * a)
# x2 = (-b - result ** 0.5) / (2 * a)
#
# if result > 0:
#     print(x1, x2)
# elif not result:
#     print(x1)
# else:
#     print("Дискриминант меньше нуля")

# == Подсчет строки и ее подстроки ==#

# str1 = input("Введи строку от 30 символов: ")
# str2 = input("Введи строку от 15 символов: ")
#
# print(f"Длина строки - {len(str1)}")
# print(f"Длина подстроки - {len(str2)}")
#
# if str2 in str1:
#     print("Подстрока есть в строке")
# else:
#     print("Подстроки такой нет")

# == Вывод корректной записи номера телефона ==#

# def create_phone_num(n):
#     return "(+{}{}) ({}{}{}) {}{}{}-{}{}{}{}".format(*n)
#
# print(create_phone_num("905392011518"))

# == Диалог ==#

# print("Как вас зовут?")
# while True:
#     flag = True
#     name = input()
#     for i in name:
#         if i.isdigit():
#             flag = False
#             print("Введите только буквы")
#             break
#     if flag:
#         break
#
# print(f"Здорово {name}, а меня зовут, Никита. Сколько тебе лет?")
#
# while True:
#     age = input("")
#     try:
#         age = int(age)
#         break
#     except ValueError:
#         print("Введите только цифры")
#
# my_age = 21
# if age < my_age:
#     print(f"Я чуть-чуть старше тебя, мне, {my_age}")
# elif age > my_age:
#     print(f"Ого! да ты старше меня на целых, {age - my_age} лет")
# else:
#     print("Надо же, мы с тобой ровестники, здорово!")
#
# print("А где ты живешь? Я живу в Москве")
# town = input()
#
# print("Чем ты увлекакшься?")
# hobbies = input().split(",")
# print(hobbies)

# == 1000-7 ==#

# i = 1000
# while i > 0:
#     print(f"{i} - 7 ? ")
#     i -= 7
# print("I am Ghoul")

# == Подсчет функции при разных значениях ==#
# for i in range(0, 11):
#     x = int(input("Введите значение X: "))
#
#     def f(a):
#         return a ** 2 + 12 * a - 50
#
#     res = f(x)
#
#     print(f"Функция F({x})=X^2+12^X-50 = {res}")

# == Сортировка по возрасту ==#
# animals = [
#     {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
#     {'type': 'elephant', 'name': 'Devon', 'age': 3},
#     {'type': 'puma', 'name': 'Moe', 'age': 5}
# ]
# print(sorted(animals, key=lambda x: x['age']))

# == Генератор паролей ==#
# import random
#
# lower_case = "qwertyuiopasdfghjklzxcvbnm"
# upper_case = "QWERTYUIOPASDFGHJKLZXCVBNM"
# numbers = "0123456789"
# symbols = "@#$%&*/\?"
#
# use_for = lower_case + upper_case + numbers + symbols
#
# length_for_pass = 10
#
# password = "".join(random.sample(use_for, length_for_pass))
#
# print(f"Your password generated: {password}")

# == Генератор Имен ==#
#
# from mimesis import Person
# from mimesis.enums import Gender
#
# person = Person('de')
#
# for i in range(0, 5):
#     print(person.full_name(Gender.MALE))

# == Рисовашка ==#

# import turtle
#
# t = turtle.Turtle()
#
# red = "red"
# orange = "orange"
# yellow = "yellow"
# green = "green"
# blue = "blue"
# purple = "purple"
#
#
# def square():
#     t.fillcolor(set_color)
#     t.begin_fill()
#
#     t.fd(100)
#     t.left(90)
#     t.fd(100)
#     t.left(90)
#     t.fd(100)
#     t.left(90)
#     t.fd(100)
#
#     t.end_fill()
#
#
# def circle():
#     t.fillcolor(set_color)
#     t.begin_fill()
#
#     t.circle(100)
#
#     t.end_fill()
#
#
# def triangle():
#     t.fillcolor(set_color)
#     t.begin_fill()
#
#     t.fd(100)
#     t.left(120)
#     t.fd(100)
#     t.left(120)
#     t.fd(100)
#
#     t.end_fill()
#
#
# def hexagon():
#     t.fillcolor(set_color)
#     t.begin_fill()
#
#     for i in range(6):
#         t.fd(90)
#         t.right(300)
#
#     t.end_fill()
#
#
# figures = ["square", "circle", "triangle", "hexagon"]
# user_figure = input(f"Выберите фигуру {figures}: ")
#
# colors = (red, orange, yellow, green, blue, purple)
# set_color = input(f"Введите каким цветом заполним фигуру: {colors}: ")
#
# pen_size = int(input("Введите толщину линии: "))
# t.pensize(pen_size)
#
# if user_figure == figures[0]:
#     square()
# if user_figure == figures[1]:
#     circle()
# if user_figure == figures[2]:
#     triangle()
# if user_figure == figures[3]:
#     hexagon()
#
# turtle.done()

# == Рисуем амогуса ==#

# import turtle
#
# # Основные цвета для персонажа
# BODY_COLOR = 'red'
# GLASS_COLOR = 'skyblue'
#
# # Главный объект
# t = turtle.Turtle()
#
#
# # Метод для рисования тела
# def body():
#     t.pensize(30)  # Размер кисти
#
#     t.fillcolor(BODY_COLOR)  # Цвет заполнения
#     t.begin_fill()
#
#     # Сторона справа
#     t.right(90)
#     t.forward(50)
#     t.right(180)
#     t.circle(40, -180)
#     t.right(180)
#     t.forward(200)
#
#     # Голова
#     t.right(180)
#     t.circle(100, -180)
#
#     # Сторона слева
#     t.backward(20)
#     t.left(15)
#     t.circle(500, -20)
#     t.backward(20)
#
#     t.circle(40, -180)
#     t.left(7)
#     t.backward(50)
#
#     t.up()
#     t.left(90)
#     t.forward(10)
#     t.right(90)
#     t.down()
#
#     t.right(240)
#     t.circle(50, -70)
#
#     t.end_fill()
#
#
# # Рисуем очки
# def glass():
#     # Передвигаем черепашку
#     t.up()
#     t.right(230)
#     t.forward(100)
#     t.left(90)
#     t.forward(20)
#     t.right(90)
#     t.down()
#
#     # Устанавливаем цвет
#     t.fillcolor(GLASS_COLOR)
#     t.begin_fill()
#
#     t.right(150)
#     t.circle(90, -55)
#
#     t.right(180)
#     t.forward(1)
#     t.right(180)
#     t.circle(10, -65)
#     t.right(180)
#     t.forward(110)
#     t.right(180)
#
#     t.circle(50, -190)
#     t.right(170)
#     t.forward(80)
#
#     t.right(180)
#     t.circle(45, -30)
#
#     t.end_fill()
#
#
# # Рисуем рюкзак
# def backpack():
#     t.up()
#     t.right(60)
#     t.forward(100)
#     t.right(90)
#     t.forward(75)
#
#     t.fillcolor(GLASS_COLOR)
#     t.begin_fill()
#
#     t.down()
#     t.forward(30)
#     t.right(255)
#
#     t.circle(300, -30)
#     t.right(260)
#     t.forward(30)
#     t.end_fill()
#
#
# # Вызываем все необходимые методы
# body()
# glass()
# backpack()
#
# turtle.done()

# == Генератор Хуимён ==#

# your_name = input("Введите имя: ")
# vowel = ["а", "и", "о", "е", "э", "ы", "я", "ё", "ю", "у"]
# for i in range(1, len(your_name)+1):
#     if your_name[i] in vowel:
#         your_name = "хуи" + your_name[i+1:]
#         break
#     else:
#         continue
#
# print(your_name)

# == Тренажер по математике ==#

'''
Сделать бесконечный(до определенной команды пользователя) генератор примеров.
В одном шаге цикла программы пользователь может выбирать тип примера(+,-,*,/ и т.д.) и количество примеров.
В соответствии с полученными данными программа поочерёдно выдаёт примеры, состоящие как минимум из двух рандомных чисел
и как минимум из одной математической операции. Пользователь вводит ответы, программа сообщает о правильности. В самом
конце программы выдаем статистику пользователя: вы решили верно 5 из 10 примеров на умножение, 4 из 12 на деление и т.д.
Последняя строка в консоли: процент верно решенных примеров на все математические операции
'''

# import random
#
# all_right_answ = 0
# all_examples = 0
#
#
# def examples(quantity, user_type, all_right, all_examples):
#     right_answ = 0
#     for i in range(quantity):
#
#         var1 = random.randint(0, 100)
#         var2 = random.randint(0, 100)
#
#         if user_type == "Вычитание":
#             answer = var1 - var2
#             u_answer = int(input(f"{var1} - {var2} = "))
#             if u_answer == answer:
#                 print("Правильно")
#                 right_answ += 1
#             else:
#                 print("Ответ не верный")
#
#         elif user_type == "Сложение":
#             answer = var1 + var2
#             u_answer = int(input(f"{var1} + {var2} = "))
#             if u_answer == answer:
#                 print("Правильно")
#                 right_answ += 1
#             else:
#                 print("Ответ не верный")
#
#         elif user_type == "Умножение":
#             answer = var1 * var2
#             u_answer = int(input(f"{var1} * {var2} = "))
#             if u_answer == answer:
#                 print("Правильно")
#                 right_answ += 1
#             else:
#                 print("Ответ не верный")
#
#         else:
#             print("Такого действия нет, прочитайте внимательно условие!")
#     print()
#     print(f"Правильно решено {right_answ} из {quantity} ({right_answ / quantity * 100}%)")
#     all_right += right_answ
#     all_examples += quantity
#     return all_right, all_examples
#
#
# while True:
#     user_type = input("""Выбери тип примера: Сложение, Умножение, Вычитание
# Если хочешь закончить, введи 'выход' """)
#     if user_type == "выход":
#         break
#     u_quantity = int(input("Выбери кол-во примеров "))
#     all_right_answ, all_examples = examples(u_quantity, user_type, all_examples, all_right_answ)
#     print(f"Общая статистика правильных отаетов: {all_right_answ / all_examples * 100}%")
#     print()


# == Сумма площадей классами ==#


# создай несколько объектов класса треугольник прямоугольник ромб + следующие функции:
# рассчет площади фигуры
# рассчет суммы площадей
# *рассчет суммы через добавление фигур в список(то есть сумма площадей фигур заранее добавленных в список)
# **добавить незамкнутые фигуры(объекты класса линия или угол), в списке проверить фигуру на наличие площади
# (то есть замкнутая ли она: например уголи или линия не замкнуты), вывести сумму замкнутых и количество не замкнутых фигур
# сделать площадь как свойство(@property)
# *координаты точек фигур(можно у одной но замкнутой) сделать неизменяемым свойством, но чтобы их можно было вывести(получить)


# label = input("Введите название фигуры (Прямоугольник, Треугольник, Круг), чтобы узнать ее периметр и площадь: \n")
# pi = 3.14
#
# print("Вводить слево наверх, направо вниз, если что-то из этого отсутствует, просто это убрать из последовательности!"
#       "Пример: Если отсутствует точка сверху, то слева направо и вниз. \n")
#
# if label == "Прямоугольник":
#     x1, y1 = map(int, input("Введите Точку А: ").split(", "))
#     x2, y2 = map(int, input("Введите Точку B: ").split(", "))
#     x3, y3 = map(int, input("Введите Точку C: ").split(", "))
#     x4, y4 = map(int, input("Введите Точку D: ").split(", "))
#
# elif label == "Треугольник":
#     x1, y1 = map(int, input("Введите Точку А: ").split(", "))
#     x2, y2 = map(int, input("Введите Точку B: ").split(", "))
#     x3, y3 = map(int, input("Введите Точку C: ").split(", "))
#
# elif label == "Круг":
#     r = int(input("Введите радиус: "))
#
#
# class Figure:
#     label = None
#
#     x1 = None
#     x2 = None
#     x3 = None
#     x4 = None
#
#     y1 = None
#     y2 = None
#     y3 = None
#     y4 = None
#
#     d1 = None
#     d2 = None
#     d3 = None
#     d4 = None
#
#     r = None
#
#     def __init__(self, label, x1=None, x2=None, x3=None, x4=None,
#                  y1=None, y2=None, y3=None, y4=None,
#                  d1=None, d2=None, d3=None, d4=None, r=None):
#         self.set_data(label, x1, x2, x3, x4, y1, y2, y3, y4, d1, d2, d3, d4, r)
#         self.get_data()
#
#     def set_data(self, label, x1, x2, x3, x4, y1, y2, y3, y4, d1, d2, d3, d4, r):
#         self.label = label
#
#         self.x1 = x1
#         self.x2 = x2
#         self.x3 = x3
#         self.x4 = x4
#
#         self.y1 = y1
#         self.y2 = y2
#         self.y3 = y3
#         self.y4 = y4
#
#         self.d1 = (((x1 - x2) ** 2) + (y1 - y2) ** 2) ** 0.5
#         self.d2 = (((x2 - x3) ** 2) + (y2 - y3) ** 2) ** 0.5
#         self.d3 = (((x3 - x4) ** 2) + (y3 - y4) ** 2) ** 0.5
#         self.d4 = (((x4 - x1) ** 2) + (y4 - y1) ** 2) ** 0.5
#
#         self.r = r
#
#         self.get_data()
#
#     def get_data(self):
#         if self.label == "Прямоугольник":
#             p_re = (self.d1 + self.d2) * 2
#             s_re = self.d1 * self.d2
#             return f"Периметр прямоугольника равен: {p_re}, Площадь прямоугольника равна: {s_re} см"
#
#         if self.label == "Треугольник":
#             p_tr = self.d1 + self.d2 + self.d3
#             p_tr_2 = p_tr / 2
#             s_tr = (p_tr_2 * (p_tr_2 - self.d1)*(p_tr_2 - self.d2)*(p_tr_2 - self.d3)) ** 0.5
#             return f"Периметр прямоугольника равен: {p_tr}, Площадь прямоугольника равна: {s_tr} см"
#
#         if self.label == "Круг":
#             p_cr = 2 * pi * r
#             s_cr = pi * (r ** 2)
#             return f"Периметр прямоугольника равен: {p_cr}, Площадь прямоугольника равна: {s_cr} см"
#
#
# if label == "Прямоугольник":
#     rectangle = Figure(label, x1, x2, x3, x4, y1, y2, y3, y4)
#     print(rectangle.get_data())
#
# elif label == "Треугольник":
#     triangle = Figure(label, x1, x2, x3, 0, y1, y2, y3, 0, 0)
#     print(triangle.get_data())
#
# elif label == "Круг":
#     circle = Figure(label, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, r)
#     print(circle.get_data())
#
# else:
#     print("ОШИБКА!!! Введите название фигуры правильно!")


# == Крестики Нолики ==#


# Реализовать программу, при помощи которой 2 игрока могут играть в
# «Крестики-нолики»на поле 3 на 3 Взаимодействие с программой
# производится через консоль. Игровое полеизображается в виде
# трех текстовых строк и перерисовывается при каждом изменении
# состояния поля. При запросе данных от пользователя программа
# cообщает, что ожидает отпользователя (в частности, координаты новой отметки на поле)
# и проверяет корректностьввода. Программа должна уметь автоматически определять,
# что партия окончена, исообщать о победе одного из игроков или о ничьей.
# Сама программа НЕ ходит, т.е. не пытается ставить крестики и нолики с целью заполнить линию


# table = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
#
#
# def p_table():
#     print(*table[0])
#     print(*table[1])
#     print(*table[2])
#
#
# win = 0
# game = 0
# main = 0
# run = 0
# player = 0
#
# while game != 1:
#
#     if player % 2 == 0:
#         print("Ход первого игрока (X)")
#     else:
#         print("Ход второго игрока (O)")
#     main = 0
#
#     while main != 1:
#         x = int(input("Введите цифру в строке: "))
#         y = int(input("Введите цифру в столбце: "))
#
#         if (int(y) < 4) and (int(y) > 0):
#             x = int(x)
#             y = int(y)
#             if (int(x) < 4) and (int(x) > 0):
#                 main = 1
#             else:
#                 print("Нет такой позиции")
#         else:
#             print("Нет такой позиции")
#
#     if (table[y - 1][x - 1] != "X") and (table[y - 1][x - 1] != "O"):
#         if player % 2 == 0:
#             table[y - 1][x - 1] = 'X'
#         else:
#             table[y - 1][x - 1] = 'O'
#
#         p_table()
#
#         for el in range(0, 3):
#             if ((table[el][0] == table[el][1] == table[el][2]) and table[el][0] != "*") or (
#                     (table[0][el] == table[1][el] == table[2][el]) and table[0][el] != "*") or (
#                     (table[0][0] == table[2][2] == table[1][1]) and table[1][1] != "*") or (
#                     (table[0][2] == table[1][1] == table[2][0]) and table[1][1] != "*"):
#                 win = 1
#
#         if win == 1:
#             print("\nИгра окончена")
#             if player % 2 == 0:
#                 print('Победил первый игрок (X)')
#             elif player % 2 != 0:
#                 print('Победил второй игрок (O)')
#             else:
#                 print("Победила дружба!")
#             game = 1
#         player += 1
#         main = 1
#
#         if run == 8:
#             print("Победила дружба")
#         else:
#             run += 1
#
#     else:
#         print("Будьте внимательнее, клетка уже занята")


#== Курс валют ==#

# import requests
# from bs4 import BeautifulSoup
# import time
#
# dollar_rub = "https://www.google.com/search?client=opera-gx&q=курс+доллара+к+рублю&sourceid=opera&ie=UTF-8&oe=UTF-8"
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0"}
#
#
# def check_currency():
#     full_page = requests.get(dollar_rub, headers=headers)
#
#     soup = BeautifulSoup(full_page.content, "html.parser")
#
#     convert = soup.findAll("span", {"class": "DFlfde SwHCTb"})
#
#     print(f"Актуальный курс 1 доллара: {convert[0].text} рублей")
#     time.sleep(3)
#     check_currency()
#
#
# check_currency()