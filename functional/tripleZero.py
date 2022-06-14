def findingTriplet(arr, n):
    triplet = False
    for i in range (0, n-2):
        for j in range (i+1, n-1):
            for k in range (j+1, n):
                if (arr[i] + arr[j] + arr[k]) == 0:
                    print ("Triplet Founded: ", end=" ")
                    print (arr[i], arr[j], arr[k])
                    triplet = True

    if triplet == False:
        print("Triplet Not Found!")

if __name__ == '__main__':
    while True:
        n = int(input("Enter Length Of An Array"))
        if n<3:
            n = int(input("Enter Valid Length Of An Array"))
        else:   
            arr = [n]
            break   

    for i in range(n):
        print("Enter ",i,": ")
        arr.append(int(input()))

    findingTriplet(arr,n)