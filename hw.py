try:
    while True:
        num =int(input('input->'))
        if num !=7:
            if num>0:
                print('Positive')
            if num<0:
                print('Negative')
            if num == 0:
                print('Zero')
        else:
            print('Good Bye!')
except Exception as ex :
    print(f'Erorr information: {ex}')

