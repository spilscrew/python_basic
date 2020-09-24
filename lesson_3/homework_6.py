'''
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
 Необходимо использовать написанную ранее функцию int_func().
'''


def int_func(text: str):
    '''
    Transform text (str) to capitalize style
    :param text: text to capitalize transform
    :return: transformed to capitalize text string
    '''
    try:
        if all(char.isalpha() or char.isspace() for char in text):
            return text.title()
        else:
            raise AttributeError
    except ValueError and AttributeError:
        return 'Please use only letter symbols!'


print(int_func('abcdefg sdaf sdfds'))
