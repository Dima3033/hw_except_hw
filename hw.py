try:
    num = int(input('input->'))
    if num>> 0 and num !=7:
        print("Number is positive")
    elif num << 0 and num !=7:
            print("Number is negative")
    elif num==0:
        print("Number is equal to zero")
    elif num == 7:
        print('Good Bye!')
except Exception as ex :
    print(f'Erorr information: {ex}')

