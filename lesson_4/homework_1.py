'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
'''

from sys import argv


def salary_calc(hours: float, rate_per_hour: float, award: float):
    '''
    Worker salary calculation
    :param hours: worked hours (float)
    :param rate_per_hour: rate per hour (float)
    :param award: award (float)
    :return: salary in currency format
    '''
    return '{:,.2f}'.format((hours * rate_per_hour) + award)


script_name, _hours, _rate_per_hour, _award = argv

try:
    _hours, _rate_per_hour, _award = float(_hours), float(_rate_per_hour), float(_award)
    if _hours >= 0 and _rate_per_hour >= 0 and _award >= 0:
        result = salary_calc(_hours, _rate_per_hour, _award)
    else:
        result = 'Please use only positive numbers or zero!'
except ValueError:
    result = 'Please use only numbers!'

print(result)
