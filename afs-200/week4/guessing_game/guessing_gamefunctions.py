import random 
print (random)

# Step 1 I need function to get a random number
def getRandomNumber(param):
    number = random.randint(1, param)
    return number

def printInfo (param):
    print ()
    print ("#"* 20)
    print( param)
    print ("*"* 20)

def promtUserForInput(mode, param):
    
    if(mode==True):
        print ("*"*40)
        print ("Start a new game =>>>")
    val =  input("<= inter 0 to exit or a number between 1 and  " +  str(param * getRandomNumber(5)) +" = " )
    return int(val)

def startGame(guess, userInput):   

    print ("*"*40)
    print ("You have selected " + str(userInput))
    if userInput == 0 :
        return False
    elif guess > userInput:
        print(" Your guess is greater. Please try again.")

    elif guess < userInput :
        print( "Your guess is smaller. Please try again")

    elif guess == userInput:
        print("!!!!! GAME OVER!!! You Guessed "+ "this many times "+ str(guess) ) 
        return  False
    return True

number = getRandomNumber(20)
#printInfo (number) 
is_user_playing = True
numberOfTries = 0

while is_user_playing:
    userInput = promtUserForInput( True,25)
    numberOfTries = numberOfTries + 1
    is_user_playing = startGame(number, userInput)
    print("You have guessed "+ str(numberOfTries) +" Times.")
    
    
        
    