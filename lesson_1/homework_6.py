'''
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. 
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
'''

ask_start_result = 'Please enter how many kilometers runner ran today:\n'
ask_end_result = 'Please enter how many kilometres runner want to handle:\n'
input_error = 'Please use only whole numbers!\n'

start_result = input(ask_start_result)
while not start_result.isnumeric():
    start_result = input(input_error + ask_start_result)
start_result = int(start_result)

end_result = input(ask_end_result)
while True:
    if not end_result.isnumeric():
        end_result = input(input_error + ask_end_result)
        continue
    elif int(end_result) <= start_result:
        end_result = input('End result must be more than start result!\n' + ask_end_result)
        continue
    else:
        end_result = int(end_result)
        break

distance_increase = 10
day = 1
while start_result <= end_result:
    start_result = start_result + start_result * 10 / 100
    round(start_result, 2)
    day += 1

print('On day ' + str(day) + ' runner will achieve the target!')