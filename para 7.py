import inspect
# import requ.ests
# import  sys
#
#
#
#
#
# class Human:
#     pass
# #
# def my_function():
#     pass
#
# print(type(requests))
# number = 10
# print(type(number))
#
#
#
#
# print(requests.__cake__)
# print(Human.__name__)
# print(my_function.__name__)
#
#
# print(dir(Human))
#
# number_list = [1,2,3]
# print(dir(number_list))
# print(hasattr(number_list, "pop"))
# print(getattr(number_list, "max" , "tyt nema Maxima"))

#

# print(inspect.ismodule(requests))
# print(inspect.isclass(requests))
# print(inspect.isfunction(my_function))
# print(inspect.getmodule(requests.get))
# print(inspect.getmodule(list))
#

















користувачі = {
    'Максим': 13,
    'Єва': 12,
    'Андрій': 14
}

# Запитуємо у користувача ім'я
ім_я = input("Будь ласка, введіть ім'я користувача: ")

# Перевіряємо, чи є таке ім'я у словнику
if ім_я in користувачі:
    print(f"Вік користувача {ім_я}: {користувачі[ім_я]} років.")
else:
    print("Користувача з таким ім'ям не знайдено у словнику.")