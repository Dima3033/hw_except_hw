try:
    list_odd = []
    list_even = []
    list_9 = []
    n1 = int(input('Число 1 - '))
    n2 = int(input('Число 2 - '))
    for i in range (n1, n2+1):
        if i % 2 == 0:
            list_even.append(i)
        elif i % 2 != 0:
            list_odd.append(i)
        elif i % 7 == 0:
            list_9.append(i)
    print(f'Even numbers: {list_even}\nsum is even: {sum(list_even)}\nAvg is even: {sum(list_even)/len(list_even)}\n')
    print(f'Even numbers: {list_odd}\nsum is even: {sum(list_odd)}\nAvg is even: {sum(list_odd)/len(list_odd)}\n')
    print(f'Even numbers: {list_9}\nsum is even: {sum(list_9)}\nAvg is even: {sum(list_9)/len(list_9)}\n')
except Exception as ex:
    print(f'Erorr information: {ex}')