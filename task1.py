num = int(input())

if num > 0:
    if num % 2 == 0:
        print('положительное четное число')
    else:
        print('положительное нечетное число')
elif num < 0:
    if num % 2 == 0:
        print('отрицательное четное число')
    else:
        print('отрицательное нечетное число')
else:
    print('нулевое число')