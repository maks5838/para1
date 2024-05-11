import inspect
import requ.ests
import  sys





class Human:
    pass
#
def my_function():
    pass
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

print(sys.executable)
print(sys.version)
print(sys.platform)
print(sys.argv)
# for module_name, module_path in sys.modules.items():
#     print(module_name, module_path)


for _ in dir(__builtins__):
    print(_)