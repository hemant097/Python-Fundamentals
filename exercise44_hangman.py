import random
words = ("apple", "banana", "cherry","orange","pineapple","coconut","pomegranate","kiwi",
         "grape", "lemon", "lime", "mango", "melon", "peach", "pear", "plum", "strawberry",
         "watermelon", "blueberry", "raspberry", "papaya", "apricot", "fig", "guava",
         "carrot", "potato", "tomato", "onion", "garlic", "broccoli", "spinach", "corn",
         "pepper", "cabbage", "cucumber", "lettuce", "mushroom", "peas", "radish", "celery",
         "eggplant", "pumpkin", "squash", "zucchini", "asparagus", "beet", "cauliflower", "kale",
         "dog", "cat", "horse", "cow", "pig", "sheep", "chicken", "duck", "turkey", "rabbit",
         "lion", "tiger", "elephant", "giraffe", "zebra", "monkey", "gorilla", "bear",
         "wolf", "fox", "deer", "moose", "kangaroo", "panda", "koala", "hippopotamus",
         "rhinoceros", "camel", "leopard", "cheetah", "whale", "dolphin", "shark", "octopus",
         "turtle", "snake", "frog", "lizard", "eagle", "owl", "parrot", "penguin",
         "butterfly", "spider", "bee", "ant", "crab", "lobster", "shrimp", "hamster", "mouse", "goat",
    "airplane", "bicycle", "helicopter", "motorcycle", "scooter", "tractor", "train", "truck",
    "bus", "boat", "rocket", "submarine", "ambulance", "taxi", "van", "wagon",
    "chair", "table", "window", "mirror", "hammer", "pencil", "bottle", "bucket",
    "candle", "pillow", "blanket", "basket", "button", "camera", "clock", "ladder",
    "bridge", "castle", "desert", "forest", "island", "mountain", "river", "volcano",
    "ocean", "garden", "valley", "canyon", "planet", "galaxy", "comet", "meteor",
    "guitar", "violin", "trumpet", "piano", "flute", "drums", "harp", "whistle",
    "doctor", "nurse", "pilot", "farmer", "cook", "baker", "singer", "dancer",
    "bread", "cheese", "pizza", "cookie", "muffin", "donut", "pasta", "burger",
    "honey", "sugar", "coffee", "juice", "butter", "yogurt", "cereal", "candy",
    "jacket", "helmet", "gloves", "shorts", "sneakers", "sandal", "glasses", "wallet",
    "circle", "square", "triangle", "diamond", "star", "heart", "cloud", "rainbow",
    "soccer", "tennis", "hockey", "skate", "ballet", "chess", "puzzle", "robot"
         )


#dictionary of key:value, integer:tuple , to display the number of incorrect guesses
hangman_art = {
    0:(" ",
       " ",
       " "),
    1:(" o ",
       " ",
       " "),
    2:(" o ",
       " | ",
       " "),
    3:(" o ",
       "/| ",
       " "),
    4:(" o ",
       "/|\\ ",
       " "),
    5:(" o ",
       "/|\\ ",
       "/ "),
    6:(" o ",
       "/|\\ ",
       "/ \\"),
}


def display_man(wrong_guesses):
    print("********************")
    for line in hangman_art[wrong_guesses]:
        print(line)#print each line of this tuple
    print("********************")


def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = [ "_" for _ in range(len(answer))] # or we can do hint=["_"]*len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:

        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Guess a letter: ").lower()

        #is length of guess !=1 OR guess is not alphabet
        if(len(guess) !=1 or not guess.isalpha()):
            print("Invalid input")
            continue

        #to avoid repeating same guess letter
        if(guess in guessed_letters):
            print(f"{guess} is already guessed")
            continue

        #storing guess in set
        guessed_letters.add(guess)

        #if guess letter is in answer(i.e., correct), replace _ in hint with the letter
        if guess in answer:
            for i in range(0,len(answer)):
                if(answer[i] == guess):
                    hint[i] = guess
        else:
            wrong_guesses += 1

        #when correctly replaced all _  OR used up all the guesses
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print(f"You win with {6-wrong_guesses} remaining guesses")
            is_running = False
        elif (wrong_guesses >= len(hangman_art) -1 ):
            display_man(wrong_guesses)
            printf(f"The correct answer was {display_answer(answer)}")
            print("You lose, better luck next time")
            is_running = False




if __name__ == "__main__":
    main()


