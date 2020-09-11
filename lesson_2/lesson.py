
variable_string = 'String' # str неизменяемый тип, коллекция, итерируемый

'''
print(variable_string[0]) # первый символ
print(variable_string[-6]) # первый символ
print(len(variable_string)) # количество символов
print(variable_string[len(variable_string) - 1]) # последний символ
print(variable_string[::-1]) # строка наоборот
print(variable_string[2:]) # начало с 3 символа
print(variable_string[:2]) # конец до 3 символа
print(variable_string[False]) # первый символ
print(variable_string[True]) # второй символ
'''

print(id(variable_string)) # id A
print(id(variable_string.lower())) # id B
print(id(variable_string.isupper())) # id c

a = 'HELLO'
b = 'HELLO'

print(a is b) # true
print(id(a) == id(b)) # true

a2 = 256
b2 = 256

print(a2 is b2) # true

list = [1, 2, 3, 4, 5, [1, 2, 3], True, False, 'HELLO']
print(type(list)) # <class 'list'>

list.append('a') # добавить в конец a
list.insert(0, 'test') # добавить в начало test
print(list)

a = (1,2,3) # кортеж, не изменяемый тип
print(type(a)) # <class 'tuple'>
b = float('inf')
print(type(b)) # <class 'float'>

variable_set = {1, 2, ('a','b')} # set множество, изменяемый, не индексируемый, ТОЛЬКО УНИКАЛЬНЫЕ ЗНАЧЕНИЯ
print(variable_set)

a = {0,1,2,3,4,True,False,None}
print(a) # {0, 1, 2, 3, 4, None} True False удалились

variable_dictionary = {'key': 'HELLO', 1: 22, (1,2): 33, True: True} # словарь
print(variable_dictionary['key']) # HELLO
variable_dictionary['test'] = 'test'
variable_dictionary.get('help', 'NOT HELP') # вернуть значение, вернуть значение если не найдено

a = 'HELLO'
for char in a:
    print(char)

for itm, value in variable_dictionary.items():
    print(itm)
    print(value)

a = [(1,2),(2,3),(3,4)]
print(dict(a))