#NUMBER GUESS GAME



import random #importing module
playing = True#initialise
number=str(random.randint(0,9))#random in built function
print("I will generate a number between 0 to 9 and you have to guess it one number at a time")
print("The game ends when you get one hero!")
#iterate loop till condition is true while playing
while playing:
    guess=input("Give me your best guess! \n")
    if number == guess:
        print("Congrants!You won")
        print("The number was",number)
        break
    else:
        print("Your guess is wrong.try again.\n")

#ROCK,PAPER,SCISSORS
import random
while True:
    user_action=input("Enter a choice[rock,paper or scissors]")
    possible_actions=["rock","paper","scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action},computer chose {computer_action}.\n")

    if user_action==computer_action:
        print(f"Both players selcted {user_action}.Its a tie")
    elif user_action=="rock":
        if computer_action=="scissors":
            print("Rock blew scissors to smitherins")
        else:
            print("Paper cover rock ,You lose")
    elif user_action=="paper":
        if computer_action=="rock":
            print("Paper covers rock,,,You won")    
        else:
            print("Rock smashes scissors.You lose")
    
    play_again=input("Play again?(y/n):")
    if play_again !="y":
        break


#ACTIVITY 3
import math
print('The floor and ceiling value of 23.56 are:'+ str(math.ceil(23.56))+','+ str(math.floor(23.56)))
x=10
y=-15

print('The value of x after copying the sign from y is: '+str(math.copysign(x,y)))

print('Absolute value of -96 and 56 are :'+str(math.fabs(-96))+','+str(math.fabs(56)))

print('The GCD of 24 and 56:'+str(math.gcd(24,56)))