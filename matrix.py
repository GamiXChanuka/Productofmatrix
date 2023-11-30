def getmatrix(x):
    """get matrix and check it  does not comply with the given dimensions"""
    matrix=[]
    print(f'Enter Matrix {x}:')
    #get matrix and check valid or invalid
    for i in range(col_len):
        row=[int(element) for element in input().split(" ")]
        if len(row)==row_len:
            matrix.append(row)
        else:
            matrix=[]
            matrix.append("Invalid Matrix")
            break #break loop when the matrix doesn't match with above mentioned dimensions
    return matrix
#-----------------------------------------
def transpose(matrix):
    """get matrix and Compute the product of the two matrices"""
    transmatrix=[] #To store transpose matrix
    for i in range(row_len):
        transmatrix_row=[] #to store one row of transpose  matrix
        for r in range(col_len):
            element=int(matrix[r][i])
            transmatrix_row.append(element)
        transmatrix.append(transmatrix_row)
    return transmatrix #return transpose matrix
#-----------------------------------------   
def product(matrix,transmatrix):
    """Compute the product of the two matrices"""
    product_matrix=[] #to store product of matrix
    for i in range(col_len):
        productmatrix_row=[] #to store one row of matrix
        for p in range(col_len):
            #counting each element
            element=0
            for r in range(row_len):
                element+=matrix[i][r] * transmatrix[r][p]
            productmatrix_row.append(element)
        product_matrix.append(productmatrix_row)
    return product_matrix #return product of matrices
#-----------------------------------------       
def printfun(matrix):
    """Prints out a formatted version of the given matrix."""
    for i in range(col_len):
        for r in range(col_len):
            print(matrix[i][r],end=" ")
        print("") #to break a rule
#-----------------------------------------
try:
    #compute and display product of two matrix
    dimension=input("Enter the dimension: ").split(",",1)
    col_len=int(dimension[0])
    row_len=int(dimension[1])
    #----------------------------------------
    matrix_a=getmatrix("A") #get matrix A
    if matrix_a[0]!="Invalid Matrix": 
        matrix_b=getmatrix("B") #get matrix B
        if matrix_b[0]!="Invalid Matrix":
            transmatrix_b=transpose(matrix_b) #call function to compute transposed matrix
            result = product(matrix_a,transmatrix_b) #get product of matrices
            printfun(result) #print product of matrices
        else:
            print("Invalid Matrix") #when second matrix was invalid
    else:
        print("Invalid Matrix") #when first matrix was invalid
        
except:
    print("Error") #For any other exceptions you are handling
