import random


def gamblerGame(stake,goal,trial):
    
    count = 1
    wins = 0

    for t in range(trial):

        cash = stake
        try:
            while cash > 0 and cash < goal :
        
              betCheck = random.randint(0,1)
          
              if betCheck == 0 :
                cash+=1
              else:                     
                cash-=1
        except:
            count+=1

        if cash == goal:
            wins+=1

    print(wins," Wins Of ", trial)
    print("Percentage of Won Game Is: ", 100.0 * wins / trial)
    print("Percentage of Loss Game Is: ", abs((100.0 * wins / trial)-100))
    print("total Number of Bets At All Time",count)


if __name__ == '__main__':
    stake = int(input("Enter Stake: "))
    goal = int(input("Enter Goal You Want Achieve: "))
    numOfTimes = int(input("Enter Number Of Times You Want To Try: "))

    gamblerGame(stake,goal,numOfTimes)