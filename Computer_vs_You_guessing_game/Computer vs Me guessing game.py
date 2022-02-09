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

# Guess the number game: You vs Computer

import random #Import random so computer can guess randomly
import time #Import time so we can pause the game to give an impression that computer is guessing (thinking) it 

numlist = [0,1,2,3,4,5,6,7,8,9,10] #The list of numbers that we must guess from

randomnum = random.choice(numlist) #Game chooses a random number from the list that we try to guess

answer = False #Our variable that shows us if anyone guessed it correctly

while answer == False: #Our while loop to keep the game going untill someone guesses the randomnum correctly
    print("It's your turn now! ")
    guess = int(input("Guess a random number between 0 and 10: ")) #Player's guess input
    counter = 1 #This counts the times we try guessing something other than a number in the list
    while guess > 10 or guess not in numlist: #This while loop checks if our guess is in the list
        print("WRONG INPUT") #If our guess is not in the list
        print("Try Again now \n") #We have to try again
        guess = int(input("Guess a random number between 0 and 10: "))
        counter +=1
        if counter > 3: #If we guess something outside the list 3 times in a row, the game ends
            print("Seems not interested in the game. GOOD BYE")
            quit()

    if guess == randomnum: #Checks if our guess is correct
        print("You are CORRECT, The number was: ", randomnum) #Tells us that we guessed it correctly and what the number was
        answer = True #Tells the game that we guessed it correctly

    else: #If our guess is not correct
        print("\nWRONG, Try again please!") #Tells us that our guess is wrong
        numlist.remove(guess) #Removes our guess from the numlist so we don't guess the same number again
        print("Numbers left in the list are: ", numlist) #Tells us what numbers are left to guess in the list

    print("\nIt's Computer's turn now!") #Tells us that computer is guessing
    guesspc = random.choice(numlist) #Computer chooses a random number from the numlist
    time.sleep(1) #We tell the game to pause for a second to give an impression that computer is guessing (thinking about) it 

    if guesspc == randomnum: #Checks if computer guessed it correctly
        print("Computer got it correct, It's luckier than you. The number was: ", randomnum, "\n") #Tells us that computer guessed it correctly and what the number was
        answer = True #Tells the game that computer guessed it correctly

    else: #If computer's guess is not correct
        numlist.remove(guesspc) #Removes computer's guess from the numlist so we don't guess the same number again
        print("The Computer guessed: ", guesspc, "\n") #Tells us what the computer guessed
        print("The numbers left in the list are: ", numlist, "\n") #Tells us what numbers are left to guess in the list
        time.sleep(1) #The game pauses for a second to let us read the list before we try to guess