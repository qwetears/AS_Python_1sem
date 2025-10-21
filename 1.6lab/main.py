from collections import Counter
text = input("Введите строку: ")
char_count = Counter(text)
print("Частоты символов:")
for char, count in char_count.items():
    print(f"'{char}': {count}")
