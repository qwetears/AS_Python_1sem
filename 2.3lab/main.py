def remove_row_col(A, K, L):  
    M = len(A)        
    N = len(A)      
        
    if K > M or L > N:  
        return A  
      
    result =   
      
    for i in range(M):  
        if i + 1 != K:  # +1 из-за индексации с 1  
            new_row =    
            for j in range(N):  
                if j + 1 != L:  
                    new_row.append(A[i][j])  
            result.append(new_row)  
      
    return result  
