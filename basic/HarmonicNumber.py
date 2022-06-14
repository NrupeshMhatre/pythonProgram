def nThHaromic (nthNum):
    
    harmonic = 0
    for i in range(2,nthNum+1):
        harmonic += 1 / i 

    return harmonic
    
if __name__ == '__main__':
    num = int(input("Enter Number To Calculate Nth harmonic Number!: \n"))
    print(nThHaromic(num))