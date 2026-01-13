import random

class Pirate:
    def __init__(self, playerNum, bidQuantity, bidValue):
        self.playerNum = playerNum
        self.dicesCount = 5
        self.dicesArr = []
        self.bidQuantity = bidQuantity
        self.bidValue = bidValue
        
    def throwDice(self):
        self.dicesArr.clear()
        
        for j in range(0, self.dicesCount):
            dice = random.randint(1, 6)
            self.dicesArr.append(dice)
            
    def removeDie(self):
        self.dicesArr.pop()
        self.dicesCount = len(self.dicesArr)
        
    def bid(self, newBidValue, newBidQuantity):
        self.bidQuantity = newBidQuantity
        self.bidValue = newBidValue
        # print("Player %i bids there will be %i dice with the value %i" % (self.playerNum, self.bidQuantity, self.bidValue))
    
    # def challenge(self):
    #     return 1    
        
    def __repr__(self):
        return "Player %i: bidQuantity - %i, BidValue - %i, DicesArr - %s" % (self.playerNum, self.bidQuantity, self.bidValue, self.dicesArr)
 
class Game:
    def __init__(self, playersCount, playersArr):
        self.currentBidValue = 0
        self.currentBidQuantity = 0
        self.diceCount = playersCount*5
        self.numberOfSameValueDice = 0
        self.lastBidderId = 1
        self.playersArr = playersArr
        
    def bidLost(self):
        self.diceCount-=1
        
    def startNewRound(self):
        self.currentBidValue = 0
        self.currentBidQuantity = 0
        self.numberOfSameValueDice = 0
        
               
playersCount = 0
  
while playersCount <= 1:  
    playersCount = int(input("Enter how may players there are: "))
    if playersCount <= 1:
        print("Please enter at least 2 players.")
        
playersArr = []

for i in range(1, playersCount+1):
    bidQuantity = 0
    bidValue = 0
    
    if i == 1:
        bidQuantity = int(input("Enter bid for the number of dice: "))
        bidValue = int(input("Enter bid for value of dice: "))
             
    player = Pirate(i, bidQuantity, bidValue)
    player.throwDice()
    playersArr.append(player)

gameObj = Game(playersCount, playersArr)

def everyoneThrowDice():
    for p in playersArr:
        p.throwDice()
  
i = 0
firstRound = True
userIsPlayer = False
# gameObj.currentBidValue = 0
# currentBidQuantity = 0
# gameObj.diceCount = 5 * playersCount

# numberOfSameValueDice = 0
# lastBidderId = 1


while len(gameObj.playersArr) > 1:
    if(firstRound):
        gameObj.currentBidValue = playersArr[0].bidValue
        gameObj.currentBidQuantity = playersArr[0].bidQuantity
        print("First player (you) bid %i dice will have the value %i" % (gameObj.currentBidQuantity, gameObj.currentBidValue))
        firstRound = False
    else:
        
        bidOrChallenge = random.randrange(0,2)
        
        if(playersArr[i].playerNum == 1):
            userIsPlayer = True
            bidOrChallenge = int(input("Enter 0 to bid or 1 to challenge!\n"))
           
        if(bidOrChallenge == 0):
            bidValueOrQuantity = random.randrange(0,2)
            
            if(userIsPlayer):
                bidValueOrQuantity = int(input("Enter 0 to bid for higher value and any amount of times or 1 to bid for more times than %i!\n" % (gameObj.currentBidQuantity)))
            
            if(bidValueOrQuantity == 0):
                newValue = random.randint(gameObj.currentBidValue+1, 6)
                newQuantity = random.randint(gameObj.currentBidQuantity, gameObj.diceCount)
                
                if(userIsPlayer):
                    newValue = int(input("Enter new value between %i and 6\n" % (gameObj.currentBidValue)))
                    newQuantity = int(input("Enter how many times this value will be met\n "))
                
                playersArr[i].bid(newValue, newQuantity)
                
                print("Player %i bids the higher value %i will come up %i times" % (playersArr[i].playerNum, newValue, newQuantity))
            else:
                newQuantity = random.randrange(gameObj.currentBidQuantity+1, gameObj.diceCount)
                
                if(userIsPlayer):
                    newQuantity = int(input("Enter how many times this value will be met\n "))
                    
                playersArr[i].bid(gameObj.currentBidValue, newQuantity)
                print("Player %i bids the same value %i will come up %i times" % (playersArr[i].playerNum, gameObj.currentBidValue, newQuantity))
                
            gameObj.lastBidderId = playersArr[i].playerNum
        else:
            print("Player %i challenges!" % (playersArr[i].playerNum))

            for p in range(0, len(playersArr)):
                for dice in playersArr[p].dicesArr:
                    if dice == gameObj.currentBidValue:
                        gameObj.numberOfSameValueDice+=1
                        
            if gameObj.numberOfSameValueDice >= gameObj.currentBidQuantity:
                print("Player %i wins the bid!" % (gameObj.lastBidderId))
            else:
                print("Player %i loses the bid!" % (gameObj.lastBidderId))
                
                for p in playersArr:
                    if p.playerNum == gameObj.lastBidderId:
                        p.removeDie()
                        gameObj.diceCount-=1
                                          
                        if(p.dicesCount == 0):
                            print("Player %i lost the game!" % (gameObj.lastBidderId))
                            playersArr.remove(p)
                            break
            
    
    userIsPlayer = False      
    
     
    if i + 1 == len(playersArr):
        i = 0
        everyoneThrowDice()
        gameObj.startNewRound()
    else:
        i+=1
        
print("Player %i is the last man standing!" % (playersArr[0].playerNum))

if(playersArr[0].playerNum == 1):
    print("You won!")
else:
    print("Better luck next time. maybe get a job or something...")

