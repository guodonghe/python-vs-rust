#!/usr/bin/python

import random

print ("Guess the number!")

secret_number = random.randint(1,101)

#print ('The secret number is: {}' .format(secret_number));


while True:


    print ("pleaee input your guess.");

   # guess = input()
    try:

        guess = input()
        print ("You guessed: {}".format(guess));

        if guess < secret_number:
            print ("Too small")
        elif guess > secret_number :
           print ("Too Big")
        else :
           print ("You win")
           break
    except:
        #guess = input()
        continue
