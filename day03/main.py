print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


path1 = input(
    "You are in the Libertalia, searching for Henry Avery's Treasure. You have to choose between the two paths in front of you. \"left\" or \"right\" ?\n"
).lower()

if path1 == "left":
    path2 = input(
        "You reach a small yet sus lake. The path continues on, on the other side of the lake. Do you want to \"swim\" or \"wait\" ?\n"
    ).lower()
    if path2 == "wait":
        path3 = input(
            "You have been rewarded for your patience and three secret portals appear in front of you. Which one do you choose? \"red\" , \"black\" or \"yellow\" ?\n"
        ).lower()
        if path3 == "red":
            print("You got burned by fire.\nGame Over.")
        elif path3 == "black":
            print("You got swallowed by an unknown darkness.\nGame Over.")
        elif path3 == "yellow":
            print(
                "You have found the long lost treasure of Libertalia.\nGame Won."
            )
    else:
        print("You got killed by an Octupus.\nGame Over.")
else:
    print("You slipped and fell off of the cliff to your death.\nGame Over.")
