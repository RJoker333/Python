list=[7,-5,-6,0,-9,10,8,-9,0,2,10,-2,10,-2,4,1,-2,-1,3,0,9,-5]
min_number=int(input("Введите минимальное значение элемента массива "))
max_number=int(input("Введите максимальное значение элемента массива "))
for i in range(len(list)):
    if min_number<=list[i]<=max_number:
        print(list[i])