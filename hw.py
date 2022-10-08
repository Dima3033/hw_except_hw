try:
    sum = 0
    while True:
        num_1 = input('num1->')
        num_2 = input('num2->')
        if num_1 < num_2:
            print(f"{num_1} is min")
        elif num_1 > num_2:
            print("{num_2} is min")
            sum+=num_1
        else:
            print('sum = ', sum)
            break
except Exception as ex :
    print(f'Erorr information: {ex}')
