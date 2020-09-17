import statistics as stat
from itertools import cycle
import time
import random
import sys
import functools

a = [itm for itm in range(2,500) if itm & 1]


def my_sum(x, y):
    return sum((x, y))


def my_pow(x, y):
    return x ** y


proc = {
    'sum': my_sum,
    'pow': my_pow
}

print(sys.argv)

# _, f, x, y = sys.argv
# print(proc[f](float(x), float(y)))
################################


def statistics():
    return 0


print(stat.mean(a))  # result 251
print(stat.median(a))  # result 251

from statistics import median as med, mean as me

print(med(a))  # result 251
print(me(a))  # result 251

tmp = ['a', 'b', 'c', 'd', 'f']

#for itm in cycle(range(10)):
#    print(itm)
#    time.sleep(1.5)
#    num = random.choice(tmp)
#    print(num)

a = [2, 3, 4, 5, 6, 7]

print(((((2 / 3) / 4) / 5) / 6) / 7)
print(functools.reduce(lambda a, b: a / b, a))