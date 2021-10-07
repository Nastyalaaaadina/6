array=[]
n=int(input('Введите количество элементов в массиве(от 1 до бесконечности) = '))
for i in range(n):
    array.append(int(input('Введите элемент массива = ')))
print(array)
delta = int(input('Введите delta = '))
r = array.count(min(array)+delta)
print(r)