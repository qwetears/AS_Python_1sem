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
b) 
