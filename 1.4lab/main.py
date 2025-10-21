n = int(input("Введите количество элементов списка: "))
lst = []
print("Введите элементы списка:")
for i in range(n):
    element = int(input(f"Элемент {i+1}: "))
    lst.append(element)

k = int(input("Введите k: "))
l = int(input("Введите l: "))

if not (1 <= k <= l <= n):
    print("Ошибка: условие 1 <= k <= l <= n не выполняется")
else:
    total = 0
    count = 0
    for i in range(k-1, l):
        total += lst[i]
        count += 1
    average = total / count
    print(f"Среднее арифметическое элементов с {k} по {l}: {average}")
