import random

low = 1
high=100
number = random.randint(1,6)
number = random.randint(low,high) #returns a random number between [a,b] (meaning both inclusive)
number = random.random() #returns a random number x in the interval [0, 1) (meaning 0<= x < 1)
# print(number)

options = ("rock","paper","scissors")
option = random.choice(options)
# print(option)

cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards)
# print(cards)

#number guessing game

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running = True

print("PYTHON NUMBER GUESSING GAME")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")
    if(not guess.isdigit()  ):
        print("Invalid guess: ")
        print(f"Please enter a number between {lowest_num} and {highest_num}")
    else:
        guess = int(guess)
        guesses += 1
        if(guess < lowest_num or guess > highest_num):
            print("Number out of range")
            print(f"Please enter a number between {lowest_num} and {highest_num}")
        elif(guess > answer):
            print("That's too high")
        elif(guess < answer):
            print("That's too low")
        else:
            print("You guessed correctly")
            print(f"You guessed in {guesses} times")
            is_running=False
