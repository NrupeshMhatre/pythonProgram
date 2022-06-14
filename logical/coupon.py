import random

def coupanGenrator(coupanCode):
   
    coupanCodeConvert = [str(i) for i in coupanCode]
       
    random.shuffle(coupanCodeConvert)

    finalCoupanCode = int("".join(coupanCodeConvert))
    return finalCoupanCode


if __name__ == '__main__':
    coupanCodeLength = int(input("Enter Coupan Code Length: "))
    coupanCode = [x for x in range(coupanCodeLength)]

    print(coupanGenrator(coupanCode))
