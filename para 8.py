# try:
#     print(123)
#     print("Hello im in try:(")
#     print(var)
# except NameError:
#     print("Помилка написання назви")
# except ZeroDivisionError as error:
#     print(error)
#
# try:
#     print(10)
# except:
#     print("Якась помилка")
#
# finally:
#     print("Не має, помилок все виконувалося успішно")


# print("Hello in out try :)")
# print(10/0)


# def checker(var):
#     if (var < 10):
#         raise ValueErrorError("Число має бути більше або дорівнювати 10")
#     else:
#         return var
#
#
# number = 10
# print(checker(number))


# class BuildingError(Exception):
#     def __str__(self):
#         return f"Введенні не вірні данні"
#
#
#
# def checker(material_count , limit):
#     if material_count < limit:
#         raise BuildingError("Матеріалів не достатньо")
#     else:
#         print("Матеріалів Достатньо")
#
# material = 120
# checker(material,   450)






































import colorama
from colorama import Fore, Back, Style
print(dir(colorama))
print("Fore атрибути:", dir(Fore))
print("Back атрибути:", dir(Back))
print("Style атрибути:", dir(Style))
