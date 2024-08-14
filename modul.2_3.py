first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and third == first and second == third:
    print(3)
elif first != second and second != third and first != third:
    print(0)
else:
    first != second or third
    print(2)