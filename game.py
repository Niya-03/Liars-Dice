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
        self.hasToBid = False
        
    def bidLost(self):
        count = 0
        for p in self.playersArr:
            count+= len(p.dicesArr)
            
        self.diceCount = count
        
    def startNewRound(self):
        self.currentBidValue = 0
        self.currentBidQuantity = 0
        self.numberOfSameValueDice = 0
        self.hasToBid = True
        
def get_int_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
                print(f"Please enter a number between {min_val} and {max_val}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")
                           
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
        bidQuantity = get_int_input("Enter bid for the number of dice: ", 1, playersCount*5)
        bidValue = get_int_input("Enter bid for value of dice: ", 1, 6)
        
             
    player = Pirate(i, bidQuantity, bidValue)
    player.throwDice()
    playersArr.append(player)

gameObj = Game(playersCount, playersArr)

def everyoneThrowDice():
    for p in gameObj.playersArr:
        p.throwDice()

i = 0
firstRound = True
userIsPlayer = False
roundStarterIndex = 0

while len(gameObj.playersArr) > 1:
    if(gameObj.playersArr[i].playerNum == 1):
        userIsPlayer = True
    else:
        userIsPlayer = False  
    
    if(firstRound):
        gameObj.currentBidValue = gameObj.playersArr[0].bidValue
        gameObj.currentBidQuantity = gameObj.playersArr[0].bidQuantity
        print("First player (you) bid %i dice will have the value %i" % (gameObj.currentBidQuantity, gameObj.currentBidValue))
        firstRound = False
    else:        
        bidOrChallenge = random.randrange(0,2)
        
        if gameObj.hasToBid: 
            gameObj.hasToBid = False
            newValue = 0
            newQuantity = 0
            
            if userIsPlayer:
                newQuantity = get_int_input("Enter bid for the number of dice: ", 1, playersCount*5)
                newValue = get_int_input("Enter bid for value of dice: ", 1, 6)
            else:
                newValue = random.randint(1, 6)
                newQuantity = random.randint(1, gameObj.diceCount)
                
            gameObj.playersArr[i].bid(newValue, newQuantity)
            gameObj.currentBidQuantity = newQuantity
            gameObj.currentBidValue = newValue
                
            print("Player %i bids the value %i will come up %i times" % (gameObj.playersArr[i].playerNum, newValue, newQuantity))
                
            if len(gameObj.playersArr)-1 == i:
                i=0
            else:
                i+=1
                    
            continue
            
        if userIsPlayer:
            bidOrChallenge = get_int_input("Enter 0 to bid or 1 to challenge!\n", 0, 1)
                 
        if(bidOrChallenge == 0):
            bidValueOrQuantity = random.randrange(0,2)
            
            if(userIsPlayer):
                bidValueOrQuantity = get_int_input("Enter 0 to bid for higher value and any amount of times or 1 to bid for more times than %i!\n" % (gameObj.currentBidQuantity), 0, 1)
            
            if(bidValueOrQuantity == 0):
                newValue = 6 if gameObj.currentBidValue == 6 else random.randint(gameObj.currentBidValue+1, 6)
                newQuantity = random.randint(gameObj.currentBidQuantity, gameObj.diceCount)
                
                if(userIsPlayer):
                    newValue = get_int_input("Enter new value between %i and 6\n" % (gameObj.currentBidValue), gameObj.currentBidValue, 6)
                    newQuantity = get_int_input("Enter how many times this value will be met\n ", 1, gameObj.diceCount)
                
                gameObj.playersArr[i].bid(newValue, newQuantity)
                gameObj.currentBidQuantity = newQuantity
                gameObj.currentBidValue = newValue
                
                print("Player %i bids the higher value %i will come up %i times" % (gameObj.playersArr[i].playerNum, newValue, newQuantity))
                
            else:
                newQuantity = gameObj.diceCount if gameObj.currentBidQuantity+1 == gameObj.diceCount else random.randrange(gameObj.currentBidQuantity+1, gameObj.diceCount)
                
                if(userIsPlayer):
                    newQuantity = get_int_input("Enter how many times this value will be met\n ", 1, gameObj.diceCount)
                    
                gameObj.playersArr[i].bid(gameObj.currentBidValue, newQuantity)
                gameObj.currentBidQuantity = newQuantity
                
                print("Player %i bids the same value %i will come up %i times" % (gameObj.playersArr[i].playerNum, gameObj.currentBidValue, newQuantity))
                
            gameObj.lastBidderId = i
        else:
            print("Player %i challenges!" % (gameObj.playersArr[i].playerNum))

            for p in range(0, len(gameObj.playersArr)):
                for dice in gameObj.playersArr[p].dicesArr:
                    if dice == gameObj.currentBidValue:
                        gameObj.numberOfSameValueDice+=1
                        
            if gameObj.numberOfSameValueDice >= gameObj.currentBidQuantity:
                #bidder wins, challenger must start
                print("Player %i wins the bid!" % (gameObj.playersArr[gameObj.lastBidderId].playerNum))
                roundStarterIndex = i
                gameObj.playersArr[i].removeDie()
                
                
                if(gameObj.playersArr[i].dicesCount == 0):
                            print("Player %i lost the game!" % (gameObj.playersArr[i].playerNum))
                                
                            del gameObj.playersArr[i]
                            
                            if i >= len(gameObj.playersArr) - 1:
                                roundStarterIndex = 0
                            else:
                                roundStarterIndex = i
                            
                            break                
            else:
                #challenger wins, bidder must start
                print("Player %i loses the bid!" % (gameObj.lastBidderId))
                                
                for idx, p in enumerate(gameObj.playersArr):
                    if p.playerNum == gameObj.playersArr[gameObj.lastBidderId].playerNum:
                        roundStarterIndex = idx
                        p.removeDie()
                                          
                        if(p.dicesCount == 0):
                            print("Player %i lost the game!" % (gameObj.playersArr[gameObj.lastBidderId].playerNum))
                            
                            gameObj.playersArr.remove(p)
                            
                            if idx >= len(gameObj.playersArr) - 1:
                                roundStarterIndex = 0
                            else:
                                roundStarterIndex = idx
                            
                            break
                                                  
            gameObj.bidLost()
            i = roundStarterIndex
            everyoneThrowDice()
            gameObj.startNewRound()
                
            continue
                      
    if i + 1 == len(gameObj.playersArr):
        i = 0
        everyoneThrowDice()
        gameObj.startNewRound()
    else:
        i+=1
        
print("Player %i is the last man standing!" % (gameObj.playersArr[0].playerNum))

if(gameObj.playersArr[0].playerNum == 1):
    print("You won!")
else:
    print("Better luck next time. maybe get a job or something...")

