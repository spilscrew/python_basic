'''
map, zip, round, sum, filter, min, max, abs, sort, reduce,
'''

a = ['1', '2', '3', '4']
b = map(int, a)
# b - <map object>
b = list(map(int, a))


def custom_map(func, obj):
    '''
    Реализация функции map
    :param func: call object
    :param obj: iterable object
    :return: list result
    '''
    result = []
    for item in obj:
        result.append(func(item))
    return result


print(custom_map.__doc__)
print(abs.__doc__)

a = [1, 2, 3, 4, 5]
b = custom_map(str, a)
c = custom_map(obj=a, func=str)

obj = ['1', '2']


def obj_append(itm, obj:list) -> list:
    obj.append(itm)
    return obj


a = [1, 2, 3, 4, 5]
b = obj_append('hello', a)
print(a)
print(b)

print(all.__doc__)
print(any((0, 0, 0, 1))) # True
print(any((0, 0, 0, 0))) # False


def func(*args, **kwargs):
    print(type(kwargs))
    print(type(args))
    print(args)


func(1, 'test', True)
print(func(1, 2, True, key='a', key2=4))


def custom_min(*args, key=lambda x: x):
    result = float('inf')
    for itm in args:
        if result > key(itm):
            result = key(itm)
    return result


def key_func(x):
    return x + 22 ** 2


print(custom_min(1, 2, 3, 4, 5, key=key_func))

print(custom_min(1, 2, 3, 4, 5, key=lambda x: x + 22 ** 2))


def template_func(template: tuple):
    def products(items):
        product = {}
        for name, item in zip(template, items):
            product[name] = item
        return product

    return products


products_1 = template_func(('name', 'quantity'))
a = products_1(('comp', 22))
print(a)

