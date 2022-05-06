def calc(vvod_1,vvod_2,vvod_3):
    if vvod_2 == '+':
        print(vvod_1+vvod_3)
    elif vvod_2 == '-':
        print(vvod_1-vvod_3)
    elif vvod_2 == '*':
        print(vvod_1*vvod_3)
    elif vvod_2 == '/':
        try:
            print(vvod_1/vvod_3)
        except ZeroDivisionError:
            print('Деление на ноль!')
        else:
            print(vvod_1/vvod_3)
vvod_2 = input('Введите операцию ')
vvod_1 = int(input('Введите первое значение '))
vvod_3 = int(input('Введите второе значение '))
count=1
while vvod_2 != 'stop':
    calc(vvod_1,vvod_2,vvod_3)
    vvod_2 = input('Введите операцию ')
    if vvod_2 != 'stop':
        vvod_1 = int(input('Введите первое число '))
        vvod_3 = int(input('Введите второе число '))
    count+=1
    print(f'Было выполнено {count}')

