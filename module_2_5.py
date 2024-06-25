# Задача "Матрица воплоти":
def get_matrix(n, m, valve):
    print('Получены параметры матрицы', n, m, valve)
    matrix = []
    if n < 0 or m < 0 or valve < 0:
        print('Числа не могут быть отрицательными')
        print(matrix)
        print()
        return

    for i in range(1, n+1):
        m1 = []
        for j in range(1, m+1): #внутренний
            m1.append(valve)
        matrix.append(m1)
    print(matrix)
    print()
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
result3 = get_matrix(4, 2, -13)