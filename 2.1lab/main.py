a) def sort_dict_by_values(input_dict):  
    sorted_asc = dict(sorted(input_dict.items(), key=lambda item: item)) [1]  
       
    sorted_desc = dict(sorted(input_dict.items(), key=lambda item: item, reverse=True)) [1]  
      
    return sorted_asc, sorted_desc  
б) def merge_dicts(dict1, dict2):   
    result = dict1.copy()  
      
    for key, value in dict2.items():  
        if key in result:   
            result[key] += value  
        else:  
            result[key] = value  
              
    return result  
в) 
