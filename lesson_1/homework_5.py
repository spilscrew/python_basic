'''
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает 
фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. 
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). 
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
'''

ask_income = 'Please, enter income:\n'
ask_cost = 'Please, enter cost:\n'
input_error = 'Please use only whole numbers!\n'

income = input(ask_income)
while not income.isnumeric():
    income = input(input_error + ask_income)
income = int(income)

cost = input(ask_cost)
while not cost.isnumeric():
    cost = input(input_error + ask_cost)
cost = int(cost)

proceeds = income - cost
if proceeds > 0:
    profit = income // cost * 100
    profit_message = 'Our monthly profit is: ' + str(profit) + '%'
    print('Congrats! Our proceeds are $' + str('{:.2f}'.format(proceeds)) + ' in this month.\n' + profit_message)

    ask_staff = 'What number of your team?\n'
    staff = input(ask_staff)
    while not staff.isnumeric():
        staff = input(input_error + ask_staff)
    staff = int(staff)
    print('Proceeds on one worker is: $' + str('{:.2f}'.format(proceeds / staff)))
elif proceeds < 0:
    print('Sorry, in this month we have loss: -$' + str('{:.2f}'.format(abs(proceeds))))
else:
    print('Nothing interesting! Our proceeds is zero.')