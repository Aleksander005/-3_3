# "Распаковка позиционных параметров"
def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params() # вызов без аргументов.
print_params(b=25) # присвоили b
print_params(c=[1, 2, 3]) # присвоили c
print_params(2, 'столбец', False) # перепросвоили всем
# print_params(1, 2,3, 4) # ошибка тк не хватает 4 элемента
print_params(b=2, c='fff') # a по умолчанию
print_params(a=0, c='ggg') # b по умолчанию
print_params(3, 'None') # c по умолчанию
list_ = (321, 333)
print_params(list_, 2, 3)  # передача картежа одному из параметров
#2
values_list = [3, 'привет', 1.2]  # список values_list с тремя элементами разных типов.
values_dict = {'a': 6, 'b': 'пока', 'c': 2.1}  # словарь values_dict с тремя ключами
print_params(*values_list)  # распаковку параметров (*
print_params(**values_dict)  # распаковку параметров (**
#3
values_list_2 = [54.32, 'Строка']  # список values_list_2 с двумя элементами разных типов
print_params(*values_list_2, 42)  # проверка , работает
