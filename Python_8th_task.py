a,b,c = int(input('Введите длину шоколадки: ')),int(input('Введите ширину шоколадки: ')),int(input('Введите кол-во долек: '))
if c%a == 0 or c%b == 0:
    print('Yes')
else: print('No')
