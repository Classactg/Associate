import random 
number = random.randint(1, 9)
print (number)
is_user_playing = True
guesses = 0

while is_user_playing:
    guess_a_number_str = input("pick_a_number")
    guesses = guesses + 1
    print (guess_a_number_str) 
    if guess_a_number_str == "exit":
        is_user_playing = False
    elif number < int(guess_a_number_str):
        print( str(guess_a_number_str) + ">is greater than")

    elif number > int(guess_a_number_str):
        print( str(guess_a_number_str) + ">is smaller than")

    elif number == int(guess_a_number_str):
        print( str(guess_a_number_str) + "> GAME OVER!!! You Guessed "+ "this many times "+ str(guesses) ) 
        is_user_playing = False
    
        
    