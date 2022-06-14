import array
def twoDArray (rows,cols):
   
    arr = []  
    for i in range(rows):  
        row = []  
        for j in range(cols):
            num = int(input("Enter the matrix"))  
            row.append(num)  
        arr.append(row)

    for i in arr:
        for j in i:
            print(j, end=" ")
        print()

twoDArray(3,2)