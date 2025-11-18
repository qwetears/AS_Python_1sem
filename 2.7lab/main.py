def copy_last_lines(input_file, output_file, K):    
    with open(input_file, 'r', encoding='utf-8') as file:  
        lines = file.readlines()  
       
    last_lines = lines[-K:]  
       
    with open(output_file, 'w', encoding='utf-8') as file:  
        file.writelines(last_lines)  
   
input_file = 'input.txt'     
output_file = 'output.txt'   
K = 3                        
  
copy_last_lines(input_file, output_file, K)  
