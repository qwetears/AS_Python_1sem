def Mean(X, Y):    
    if X <= 0 or Y <= 0:  
        raise ValueError("Числа должны быть положительными")  
      
    AMean = (X + Y) / 2  
        
    import math  
    GMean = math.sqrt(X * Y)  
      
    return AMean, GMean  
