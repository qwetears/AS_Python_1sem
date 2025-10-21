n = int(input("Введите натуральное число n: "))

sum_result = 0
for i in range(1, n + 1):
    sum_result += 1 / (2 ** i)

print(f"Сумма ряда: {sum_result}")
