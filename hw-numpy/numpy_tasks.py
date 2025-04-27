import numpy as np

def uniform_intervals(a, b, n):
    """1. создает numpy массив - равномерное разбиение интервала от a до b на n отрезков."""
    return np.linspace(a, b, n)

def cyclic123_array(n):
    """2. Генерирует numpy массив длины  3n , заполненный циклически числами 1, 2, 3, 1, 2, 3, 1...."""
    seq = np.array([1, 2, 3])
    cyclic_array = np.tile(seq, n)
    return cyclic_array

def first_n_odd_number(n):
    """3. Создает массив первых n нечетных целых чисел"""
    odds = np.arange(1, 2*n, 2)
    return odds

def zeros_array_with_border(n):
    """4. Создает массив нулей размера n x n с "рамкой" из единиц по краям."""
    matrix = np.ones((n, n), dtype=int)
    if n > 2:
        matrix[1:-1, 1:-1] = 0
    return matrix

def chess_board(n):
    """5. Создаёт массив n x n с шахматной доской из нулей и единиц"""
    indices = np.indices((n, n))
    chessboard = (indices[1] + indices[0] + 1) % 2
    return chessboard

def matrix_with_sum_index(n):
    """6. Создаёт nxn матрицу с (i,j)-элементами равным i+j."""
    row_indices = np.arange(n).reshape(n, 1)
    col_indices = np.arange(n)
    matrix = row_indices + col_indices
    return matrix

def cos_sin_as_two_rows(a, b, dx):
    """7. Вычислите $cos(x)$ и $sin(x)$ на интервале [a, b) с шагом dx,
    а затем объедините оба массива чисел как строки в один массив. """
    x_values = np.arange(a, b, dx)
    cos_values = np.cos(x_values)
    sin_values = np.sin(x_values)
    result_array = np.vstack((cos_values, sin_values))
    return result_array


def compute_mean_rowssum_columnssum(A):
    """8. Для numpy массива A вычисляет среднее всех элементов, сумму строк и сумму столбцов."""
    meanval = A.mean()
    cols = A.sum(axis=1)
    rows = A.sum(axis=0)

    return meanval, rows, cols

def sort_array_by_column(A, j):
    """ 9. Сортирует строки numpy массива A по j-му столбцу в порядке возрастания."""
    sorted_A = A[A[:, j].argsort()]
    return sorted_A

def compute_integral(a, b, f, dx, method):
    """10. Считает определённый интеграл функции f на отрезке [a, b] с шагом dx 3-мя методами:
    method == 'rectangular' - методом прямоугольника
    method == 'trapezoidal' - методом трапеций
    method == 'simpson' - методом Симпсона
    """
    x = np.arange(a, b + dx, dx)
    if x[-1] > b:
        x = x[x <= b]
    n = len(x) - 1
    if method == 'rectangular':
        x_rect = x[:-1]
        compute = np.sum(f(x_rect)) * dx
    elif method == 'trapezoidal':
        compute = (dx/2) * (f(x[0]) + f(x[-1]) + 2 * np.sum(f(x[1:-1])))
    elif method == 'simpson':
        if n % 2 == 1:
            x = x[:-1]
            n = n - 1
        f_values = f(x)
        compute = dx/3 * (f_values[0] +
                                4 * np.sum(f_values[1:n:2]) +
                                2 * np.sum(f_values[2:n-1:2]) +
                                f_values[-1])

    return compute

np.random.seed(42)
A = np.random.rand(3, 5)
print(compute_mean_rowssum_columnssum(A))
