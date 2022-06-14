import math
def factor (n):
    primeFactor = []
    divisor = 2
    while divisor <= n:
        if n%divisor == 0:
            primeFactor.append(divisor)
            n = n/divisor
        else:
            divisor+=1
    return primeFactor
if __name__ == '__main__':
    num = int(input("Enter Number To Factors Of Number!: \n"))
    print("Factors Of ", num ," Is: ", factor(num))