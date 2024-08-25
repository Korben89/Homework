stoun_1 = 21
for n in range(3, stoun_1):
    result = str()
    for i in range(1, stoun_1):
        for j in range(i+1, stoun_1):
           if n % (i + j) == 0:
               result += f"{i}{j}"
    print(f'{n} - {result}')
