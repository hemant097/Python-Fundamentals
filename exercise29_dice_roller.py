import random
# print("\u25CF \u250c \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘


"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"
       ),
    2:("┌─────────┐",
       "│  ●      │",
       "│         │",
       "│      ●  │",
       "└─────────┘"
       ),
    3:("┌─────────┐",
       "│ ●       │",
       "│    ●    │",
       "│       ● │",
       "└─────────┘"
       ),
    4:("┌─────────┐",
       "│  ●   ●  │",
       "│         │",
       "│  ●   ●  │",
       "└─────────┘"
       ),
    5:("┌─────────┐",
       "│  ●   ●  │",
       "│    ●    │",
       "│  ●   ●  │",
       "└─────────┘"
       ),
    6:("┌─────────┐",
       "│  ●   ●  │",
       "│  ●   ●  │",
       "│  ●   ●  │",
       "└─────────┘"
       )
    }

dice = []
total=0

num_of_dice = int(input("How many dice?"))

#generates random ints and appends in dice[]
for die in range(num_of_dice):
    dice.append(random.randint(1,6))

print(dice)

#gets the corresponding dice art for each number in dice[], in vertical manner
for die in range(0,num_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)

# to get the die printed horizontally, we need to iterate over dice_art. Suppose dice[] is [3,4,2] This'll work like, first it'll
# print the first line of dice_art of 3,4,2 and then second .....5th line (as each dice_art is of 5 lines)
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line],end=" ")
    print()

for die in dice:
    total+=die

print(f"You got {total} ")