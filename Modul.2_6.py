def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        a = [value] * m
        matrix.append(a)
    return matrix
result1 = get_matrix(5, 7, 3000)
result2 = get_matrix(2, 6, 'Python')
result3 = get_matrix(3, 3, 7)
print(result1)
print(result2)
print(result3)
