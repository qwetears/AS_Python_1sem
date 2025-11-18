def product_of_file(filename):  
    try:  
        with open(filename, 'r') as file:   
            lines = file.readlines()  
                
            product = 1.0  
               
            for line in lines:  
                try:   
                    number = float(line.strip())   
                    product *= number  
                except ValueError:  
                    print(f"Предупреждение: строка '{line.strip()}' не является числом и будет пропущена")  
                      
        return product  
      
    except FileNotFoundError:  
        print(f"Ошибка: файл '{filename}' не найден")  
        return None  
    except Exception as e:  
        print(f"Произошла ошибка: {str(e)}")  
        return None  
