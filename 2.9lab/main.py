import numpy as np  
 
def read_matrices(filename):  
    with open(filename, 'rb') as f:    
        count = np.fromfile(f, dtype=np.int32, count=1)  
        m, n = np.fromfile(f, dtype=np.int32, count=2)  
        matrices = np.fromfile(f, dtype=np.float64).reshape(count, m, n)  
    return matrices, m, n  
   
def write_matrices(filename, matrices, m, n):  
    with open(filename, 'wb') as f:  
        np.array([len(matrices)], dtype=np.int32).tofile(f)  
        np.array([m, n], dtype=np.int32).tofile(f)   
        matrices.astype(np.float64).tofile(f)  
    
matrices1, m, n = read_matrices('file1.bin')  
matrices2, _, _ = read_matrices('file2.bin')  
   
zero_matrices = matrices1[matrices1[:, 0, 0] == 0]  
    
remaining_matrices1 = matrices1[matrices1[:, 0, 0] != 0]  
   
matrices2 = np.concatenate((matrices2, zero_matrices))  
  
write_matrices('file1.bin', remaining_matrices1, m, n)  
write_matrices('file2.bin', matrices2, m, n)  
   
print("Содержимое первого файла:")  
for i, matrix in enumerate(remaining_matrices1):  
    print(f"Матрица {i+1}:")  
    print(matrix)  
    print()  
  
print("\nСодержимое второго файла:")  
for i, matrix in enumerate(matrices2):  
    print(f"Матрица {i+1}:")  
    print(matrix)  
    print()  
