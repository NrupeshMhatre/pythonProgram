def powerOfTwo (nthNum):
    ansNum = 1
    for i in range(nthNum):
        ansNum = ansNum * 2
        print( " 2 Power Of ", i+1 , " is   : " ,ansNum)
if __name__ == '__main__':
    while True:
        num = int(input("Enter Number To Print Power Of Two Till Number!: \n"))
        if num>31 and num<0:
            num = int(input("Please, Enter Number Less Than 31 "))
            powerOfTwo(num)
            break
        else:
            powerOfTwo(num)
            break