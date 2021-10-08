print("Введите размер массива.")
g = int(input())
a = [0] * g
for i in range(len(a)):
    i = str(i + 1)
    print("Введите элемент массива " + i)
    i = int(i)
    i = i - 1
    a[i] = int(input())
min = a[1]
for i in range(len(a)):
  if (a[i]<min):
    min = a[i]
print("Минимальное значение массива =",min)
print("Введите число DELTA")
delta = int(input())
y = min + delta
t = 0
for i in range(len(a)):
    if (a[i]==y):
        t = t + 1
if (t==0):
    print("Элементов  в  заданном  массиве, отличающихся от минимального на DELTA - нет.")
else:
    print("Количество таких чисел =", t)