а) def full_name(first_name, last_name, middle_name=None):  
    if middle_name:  
        return f"{last_name} {first_name} {middle_name}"  
    else:  
        return f"{last_name} {first_name}"   
б) def transform_list(numbers, transform_function=None):  
    if transform_function is None:  
        return numbers.copy()  
      
    return [transform_function(num) for num in numbers]    
original_list = [1, 2, 3, 4, 5]  
result1 = transform_list(original_list)  
print(result1)  
  
 
def multiply_by_two(x):  
    return x * 2  
  
result2 = transform_list(original_list, multiply_by_two)  
print(result2)    
    
def square(x):  
    return x ** 2  
  
result3 = transform_list(original_list, square)  
print(result3)  
в) def sum_positive_numbers(*args):   
    return sum(num for num in args if num > 0)  
г) def common_keys(**kwargs):  
    if not kwargs:  
        return {}  
      
    dicts = kwargs.values()  
      
    common = set(dicts.keys())  
    for d in dicts[1:]:  
        common.intersection_update(d.keys())  
      
    result = {key: dicts[key] for key in common}  
    return result  
