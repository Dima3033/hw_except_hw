import math
try:
    list = []
    while True:
        num = int(input('Число  - '))
        if num != 7:
            list.append(num)
        else:
         print(f' Sum: {sum(list)}\n Max: {max(list)}\n Min: {min(list)}\n Good Bye! ')
except Exception as ex:
    print(f'Erorr information: {ex}')
