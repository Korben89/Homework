def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 'Рука', False]
values_dict = {'a': 6, 'b': 'Криветка', 'c': False}
values_list_2 = [7, 'Рубашка']

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
