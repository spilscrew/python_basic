'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
'''

from typing import List


class Matrix:
    def __init__(self, rows: List[List[int]]):
        self.__rows = rows
        self.validation(self.__rows)
        self.rows_count = len(rows)
        self.columns_count = max(len(row) for row in self.__rows)
        for row in self.__rows:
            if len(row) < self.columns_count:
                row += (self.columns_count - len(row)) * [0]

    def validation(self, rows):
        try:
            for row in rows:
                if not isinstance(row, list):
                    raise TypeError
                for val in row:
                    if not isinstance(val, int):
                        raise ValueError
        except TypeError:
            print('Matrix rows must be lists!')
            del self
        except ValueError:
            print('Matrix rows values must be integers!')
            del self

    def __str__(self):
        result = str()
        for row in self.__rows:
            row = str(row).replace('[', '').replace(']', '').replace(',', '') + '\n'
            result += row
        return result

    def __add__(self, other):
        if isinstance(other, Matrix):
            if not self.columns_count == other.columns_count and self.rows_count == other.rows_count:
                raise ValueError(f'Matrix shape are not equal!')

            result = []
            for row_index, row in enumerate(self.__rows):
                result.insert(row_index, [])
                for itm_index, itm in enumerate(row):
                    result[row_index].insert(itm_index, itm + other.__rows[row_index][itm_index])

            return Matrix(rows=result)
        else:
            print('Must be Matrix() types for sum!')
            return ''


matrix_1 = Matrix(rows=[[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]])
print(matrix_1)

matrix_2 = Matrix(rows=[[10, 20, 30], [40, 50, 60], [70, 80, 90, 100]])
print(matrix_2)

matrix_3 = Matrix(rows=[[100, 200, 300], [400, 500, 600], [700, 800, 900, 1000]])
print(matrix_3)

matrix_sum = matrix_1 + matrix_2 + matrix_3
print('*** 1 + 2 + 3 ***')
print(matrix_sum)
print('*****************')

matrix_sum = matrix_1 + matrix_2
print('*** 1 + 2 ***')
print(matrix_sum)
print('*************')

matrix_sum = matrix_1 + matrix_3
print('*** 1 + 3 ***')
print(matrix_sum)
print('*************')

