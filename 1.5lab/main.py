n = int(input("Введите количество элементов: "))
numbers = []

print("Введите элементы списка:")
for i in range(n):
    num = int(input(f"Элемент {i+1}: "))
    numbers.append(num)

odd_numbers = [x for x in numbers if x % 2 != 0]
result = sorted(odd_numbers, reverse=True)

print(f"\nИсходный список: {numbers}")
print(f"Нечетные числа: {odd_numbers}")
print(f"Отсортированные по убыванию: {result}")
