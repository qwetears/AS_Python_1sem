a) try:  
    number = float(input("Введите число: "))  # Получаем число от пользователя  
      
    if number < 0:  
        raise ValueError("Число должно быть положительным")  
    elif number == 0:  
        raise ZeroDivisionError("Число не может быть нулевым")  
    else:  
        print("Число введено корректно")  
  
except ValueError as ve:  
    print(f"Ошибка: {ve}")  
except ZeroDivisionError as zde:  
    print(f"Ошибка: {zde}")  
б) def check_age(age):  
    try:  
        age = int(age)  # Преобразуем ввод в целое число  
          
        if age < 18:  
            raise ValueError("Несовершеннолетний пользователь")  
        elif age > 100:  
            raise ValueError("Неверный возраст")  
        else:  
            print("Возраст введен корректно")  
              
    except ValueError as e:  
        print(f"Ошибка: {e}")  
  
# Пример использования:  
user_age = input("Введите ваш возраст: ")  
check_age(user_age)  
в) try:  
    number = float(input("Введите число: "))  
    assert number >= 0, "Число должно быть положительным"  
    print("Число введено корректно")  
except AssertionError as e:  
    print(e)  
