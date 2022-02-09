'''
------------------------------------------------------------
-------------A-------------EEEEEEEEEE-----YYY-------YYY-----
------------AAA------------EEE-------------YYY-----YYY------
-----------AAAAA-----------EEE--------------YYY---YYY-------
----------AAA-AAA----------EEE---------------YYY-YYY--------
---------AAA---AAA---------EEEEEEEEEE---------YYYYY---------
--------AAA-----AAA--------EEE-----------------YYY----------
-------AAAAAAAAAAAAA-------EEE-----------------YYY----------
------AAA---------AAA------EEE-----------------YYY----------
-----AAA-----------AAA-----EEEEEEEEEE----------YYY----------
------------------------------------------------------------
'''

# Guess the number game: Computer vs Computer (Jack Sparrow vs Barbarosa because I love Pirates of the Caribbean)

import random #Import random so computer can guess randomly
import time #Import time so we can pause the game to give an impression that computer is guessing (thinking) it 

numlist = [0,1,2,3,4,5,6,7,8,9,10] #The list of numbers that we must guess from
randomnum = random.choice(numlist) #Game chooses a random number from the list that we try to guess

answer = False #Our variable that shows us if anyone guessed it correctly

while answer == False: #Our while loop to keep the game going untill someone guesses the randomnum correctly
    print("It's Jack Sparrow's turn now! ") #Tells us who's turn it is right now
    guesspc_Jack = random.choice(numlist) #Computer chooses a random number from the numlist
    time.sleep(3) #We tell the game to pause for 3 seconds to give an impression that computer is guessing (thinking about) it 
    
    if guesspc_Jack == randomnum: #Checks if computer guessed it correctly
        print("Jack Sparrow got it correct, What a great captain! The number was: ", randomnum, "\n") #Tells us that computer guessed it correctly and what its guess was
        answer = True #Tells the game that computer guessed it correctly
        quit() #Exits the game

    else: #If computer's guess is not correct
        print("Jack guessed it incorrectly, his guess was: ", guesspc_Jack) #Tells us that computer guessed it incorrectly and what its guess was
        numlist.remove(guesspc_Jack) #Removes computer's guess from the numlist so they don't guess the same number again
        print("Numbers left in the list are: ", numlist, "\n") #Tells us what numbers are left to guess in the list

    print("It's Barbarosa's turn now!") #Tells us who's turn it is right now
    guesspc_Barbarosa = random.choice(numlist) #Computer chooses a random number from the numlist
    time.sleep(3) #We tell the game to pause for 3 seconds to give an impression that computer is guessing (thinking about) it 

    if guesspc_Barbarosa == randomnum: #Checks if computer guessed it correctly
        print("Barbarosa got it correct, What a great captain! The number was: ", randomnum) #Tells us that computer guessed it correctly and what its guess was
        answer = True #Tells the game that computer guessed it correctly
        quit() #Exits the game

    else: #If computer's guess is not correct
        numlist.remove(guesspc_Barbarosa) #Removes computer's guess from the numlist so they don't guess the same number again
        print("Barbarosa guessed it incorrectly, his guess was: ", guesspc_Barbarosa) #Tells us that computer guessed it incorrectly and what its guess was
        print("The numbers left in the list are: ", numlist, "\n") #Tells us what numbers are left to guess in the list
        time.sleep(1) #The game pauses for a second switch turns