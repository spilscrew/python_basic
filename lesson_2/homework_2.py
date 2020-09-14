'''
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2
и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input().
'''

ask_elements_length = 'Please enter number of elements:\n'
ask_data = 'Please enter data:\n'
input_error = 'Please enter whole number!\n'

elements_length = input(ask_elements_length)
while not elements_length.isdigit():
    elements_length = input(input_error + ask_elements_length)
elements_length = int(elements_length)

counter = 1
data_list = []
while elements_length >= counter:
    data = input('Please enter #' + str(counter) + ' data:\n')
    data_list.append(data)
    counter += 1

print('Normal data list: ' + str(data_list))

modified_data_list = []
for index in range(len(data_list)):
    if index + 1 == elements_length and not (elements_length % 2) == 0:
        modified_data_list.append(data_list[index])
        break
    if (index % 2) == 0:
        modified_data_list.append(data_list[index + 1])
    else:
        modified_data_list.append(data_list[index - 1])

print('Modified data list: ' + str(modified_data_list))