# Treasure Quest Scenes
print("⚔︎ Treasure Quest ⚔︎\n")

# Intro description:
print("You are a treasure hunter who is on a quest to find hidden treasures left by four ancient kings, its" \
"been hidden for centeries and no one has been able to find it, but you wont give up! The only clue the ancient kings" \
"left behind was a stone tablet with different symbols on it, you remember seeing these symbols on your grand mothers" \
"vase that she never let you touch. One day, while she was out getting groceries to make cookies, you decided to climb" \
"on top of the counter to get the vase down, you grabbed the vase and carefully climb down, you inpectthe vase and the" \
"four symbols on it, you look closer at the small writing underneath each symbol, they read: North (Treasure of Winter)," \
"East(Treasure of autumn), South(Treasure of spring) and west (treasure of summer), these are directions! You put the" \
"vase back then decide to set out on your quest to find the hidden treasures")


# Game starts
# (Tutorial)
print("\nType in the number to the choice you want to make.\n")

# Choices:
print("1. North (Treasure of Winter)" "\n"
      "2. East  (Treasure of Autumn)" "\n"
      "3. South (Treasure of Spring)" "\n"
      "4. West  (Treasure of Summer)" "\n")


while True:
    choice = input("What direction should go to?")

    if choice == "1":
        print("You set sail to the North!\n")
        
        
    elif choice == "2":
        print("You chose East (Treasure of Autumn)")
        break
    elif choice == "3":
        print("You chose South (Treasure of Spring)")
        break
    elif choice == "4":
        print("You chose West (Treasure of Summer)")
        break
    else:
        print("Invalid choice. Please try again.")



def Winter_island():
    print("You set sail to the North!\n")
    print("after days of sailing you reach an island directly North of your home, you dock your ship, " \
"cold, arctic winds hit you face, good thing you prepared for this, you walk inland and see a huge " \
"mountain in the distance, you start to make your way to the mountain as big as mount everest, " \
"after hours of hiking you reach the base of the mountain, you see a cave entrance, you brush off " \
"some snow from a fallen boulder next to it and see a blue gemstone engraved in the rock, you enter " \
"the cave, its dark and cold, you walk deeper into the cave until you see a peice of meat laying " \
"on the ground, you are very hungry from your voyage," "\n")
    
choice = input("Do you eat the meat?")   

print("5. Eat the meat")
print("6. Move on into the cave\n")
    

def Meat_Scene():
    print("You go to pick up the meat, as you do a huge polar bear jumps out from the shadows and attacks you, you try")
    print("to fight it off but it overpowers you.\n")

def Game_Over():
    print("You have failed your quest.\n")

if choice == "5":
    return Meat_Scene()
else:
    return Game_Over()
        
