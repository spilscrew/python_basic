result = []

for itm in range(10):
    if itm & 1:
        result.append(itm)
print(result)

result_2 = [itm for itm in range(10) if itm & 1]  # comprehension
print(result_2)

result_3 = [(itm, n) for itm in range(10) for n in range(10, 20)]  # comprehension
print(result_3)

result_4 = tuple((itm, n) for itm in range(10) for n in range(10, 20))
print(result_4)

'''
def custom_map(func, iter_obj):
    for _ in iter_obj:
        yield func(_)  # yield - возврат промежуточных значений


tmp = custom_map(lambda x: x ** 2, range(3))
print(list(tmp))
print(next(tmp))

tmp = custom_map(lambda x: x ** 2, range(3))
while True:
    try:
        item = next(tmp)
    except StopIteration:
        break
    print(item + ' bloo')
'''


def some(x):
    yield x - 2
    yield x - 3
    yield x - 4


tmp = some(10)
for itm in tmp:
    print(itm)


def rec(*args):
    return args[-1] + rec(*args[:-1]) if args else 0


print(rec(1, 2, 3, 4, 5, 6, 7))