def midpoint(x1, y1, x2, y2):  
    return ((x1 + x2) / 2, (y1 + y2) / 2)  
  
  
def can_form_triangle(a, b, c):  
    return a + b > c and a + c > b and b + c > a  
  
  
def triangle_area(a, b, c):  
    p = (a + b + c) / 2  
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5  
  
  
# Пример использования модуля  
if __name__ == "__main__":  
    # Пример 1: Середина отрезка  
    x1, y1 = 1, 2  
    x2, y2 = 4, 6  
    mid = midpoint(x1, y1, x2, y2)  
    print(f"Середина отрезка: {mid}")  
  
    # Пример 2: Проверка построения треугольника  
    a, b, c = 3, 4, 5  
    if can_form_triangle(a, b, c):  
        print(f"Треугольник со сторонами {a}, {b}, {c} можно построить")  
    else:  
        print(f"Треугольник со сторонами {a}, {b}, {c} построить нельзя")  
  
    # Пример 3: Площадь треугольника  
    area = triangle_area(a, b, c)  
    print(f"Площадь треугольника: {area:.2f}")  
