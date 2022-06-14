import random
from pip import __main__

def flipPercentage(head,tail):
    
    totalToss = head+tail

    headPercentage = 100 * head / totalToss

    print ("Percentage Of Head is", headPercentage)

    print ("Percentage Of Tail is", abs(headPercentage-100))

def coinFlipCalculation(totalFlip):
    
    head = 0
    tail = 0

    for i in range (totalFlip):
        flipCheck = random.randint(0,1)

        if flipCheck == 0:
            head+=1
        else:
            tail+=1
    
    print("Total Head Is ",head)
    print("Total Tail Is ",tail)
    flipPercentage(head,tail)


if __name__ == '__main__':
    
    numOfFlip = int(input("Enter How Many Time Wanna Flip! \n"))
    coinFlipCalculation(numOfFlip)