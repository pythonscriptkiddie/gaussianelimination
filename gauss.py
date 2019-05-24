def do_swap(matrix, j):
    if matrix[j][j] == 0:
        original_row = matrix[j] 
        for k, row in enumerate(matrix[j + 1:], j+1):
            if row[j] != 0:
                new_row_copy = row.copy()
                original_row_copy = original_row.copy()
                matrix[j] = new_row_copy
                matrix[k] = original_row_copy
                return matrix
                
                
def gauss(A):
    '''Solving a n x n+1 augmented matrix'''
    for j,row in enumerate(A):
        #diagonal term to be 1
        #by dividing row by diagonal term
        #row swap
        do_swap(A, j)
        if row[j] != 0:
            divisor = row[j]
            for i,term in enumerate(row):
                row[i] = term / divisor
            
        #add the other rows to additive inverse to make value 0
        rowList = [x for x in range(len(A))]
        rowList.remove(j)
        for i in rowList:
            addinv = -1*A[i][j]
            for ind,value in enumerate(A[i]):
                A[i][ind] = value + addinv*A[j][ind]
                
    return A

if __name__ == '__main__':

    B = [[2,1,-1,8],[-3,-1,2,-1],[-2,1,2,-3]]
    
    d = gauss(B)
    
    for i in d:
        print(i, sep='\n')


        
