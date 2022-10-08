try:
    sum = 0
    while True:
        num = int(input('input->'))
        if num != 7:
            if num > 0:
                print("Number is positive")
            if num < 0:
                print("Number is negative")
            if num == 0:
                print("Number is equal to zero")
            sum+=num
        else:
            print('sum = ', sum)
            break
except Exception as ex :
    print(f'Erorr information: {ex}')

