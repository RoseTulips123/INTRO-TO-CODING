
print("⚔︎ Treasure Quest ⚔︎\n")


print("You are a treasure hunter who is on a quest to find hidden treasures left by four ancient kings, its" \
"been hidden for centeries and no one has been able to find it, but you wont give up! The only clue the ancient kings" \
"left behind was a stone tablet with different symbols on it, you remember seeing these symbols on your grand mothers" \
"vase that she never let you touch. One day, while she was out getting groceries to make cookies, you decided to climb" \
"on top of the counter to get the vase down, you grabbed the vase and carefully climb down, you inpectthe vase and the" \
"four symbols on it, you look closer at the small writing underneath each symbol, they read: North (Treasure of Winter)," \
"East(Treasure of autumn), South(Treasure of spring) and west (treasure of summer), these are directions! You put the" \
"vase back then decide to set out on your quest to find the hidden treasures")



print("\nType in the number to the choice you want to make.\n")

chosen_direction = input("What direction should you go first?\n"
                         "1. North (Treasure of Winter)\n"
                         "2. East  (Treasure of Autumn)\n"
                         "3. South (Treasure of Spring)\n"
                         "4. West  (Treasure of Summer)\n")



def choose_direction():
        if chosen_direction == "1":
               print("You set sail to the North!\n")
               return north_scene()
        elif chosen_direction == "2":
                print("You set sail to the East!\n")
                return east_scene()
        elif chosen_direction == "3":
                print("You set sail to the South!\n")
                return south_scene()
        elif chosen_direction == "4":
                print("You set sail to the West!\n")
                return west_scene()
        else:
                print("Invalid choice. Please try again.")
                choose_direction()
    
def north_scene():    
   print("after days of sailing you reach an island directly North of your home, you dock your ship,")
print("cold, arctic winds hit you face, good thing you prepared for this, you walk inland and see a huge")
print("mountain in the distance, you start to make your way to the mountain as big as mount everest,")
print("after hours of hiking you reach the base of the mountain, you see a cave entrance, you brush off")
print("some snow from a fallen boulder next to it and see a blue gemstone engraved in the rock, you enter")
print("the cave, its dark and cold, you walk deeper into the cave until you see a peice of meat laying")
print("on the ground, you are very hungry from your voyage," "\n")
choice = input("Do you eat the meat?\n"
               "5. Eat the meat\n"
               "6. Move on into the cave\n")   

if choice == "5":
        print("You go to pick up the meat, as you do a huge polar bear jumps out from the shadows and attacks you, you try")
        print("to fight it off but it overpowers you.\n")
        print("You have failed your quest.")
        north_scene()
        

if choice == "6":
        print("You ignore the meat and walk deeper into the cave, after a few minutes you see a light in the distance, you")
        print("walk towards it and find a large chamber with the floor frozen over, you see a large ice pedestal in the center")
        print("of the chamber with a chest on top of it, should you cross the frozen floor to get to the chest? Or look around")
        print("the chamber first?")

else:
        print("Invalid choice. Please try again.")
        north_scene()

choice = input("7. Cross the frozen floor to the chest\n"
               "8. Look around the chamber first\n")

if choice == "7":
        print("You make your way across the frozen floor, as you near the pedestal you hear a cracking sound, before you can")
        print("react the ice breaks beneath you, and you fall into freezing water below, the freezing temperature of the water")
        print("gives you hypothermia and you drown.\n")
        print("You have failed your quest.")
        north_scene()

if choice == "8":
      print("You observe the ice closely and see that the floor is very thin in some spots, you carefully make your way across")
      print("the chamber avoiding the thin ice, you reach the pedestal and open the chest, inside you find gold, diamonds,")
      print("a sheild, and a Blue gemstone!\n")
      print("Congratulations! You have found the Treasure of Winter!\n")

choose_direction2 = input("What direction should you like to go to next?")
print("9. East  (Treasure of Autumn)") 
print("10. South (Treasure of Spring)") 
print("11. West  (Treasure of Summer)\n") 

def choose_direction2():
        if choose_direction2 == "9":
               print("You set sail to the East!\n")
               return east_scene()
        elif choose_direction2 == "10":
                print("You set sail to the South!\n")
                return south_scene()
        elif choose_direction2 == "11":
                print("You set sail to the West!\n")
                return west_scene()
        else:
                print("Invalid choice. Please try again.")
                choose_direction2()

def east_scene():
       print("Upon arriving at the island directly East of your home, you immediately see beautiful mountainous terrain") 
       print("and colorful trees, you see two paths ahead of you, one leading into a beautiful forest, and one leading")
       print("towards a treehouse village built into the mountainside, which path do you take?\n") 

choice = input("Which path do you take?\n")
print("12. Enter the forest")
print("13. Head towards the treehouse village\n")

def forest_path():  
        print("You enter the forest, the trees are tall and the leaves are a beautiful array of reds, oranges, and yellows, as you")
        print("walk deeper into the forest you see a clearing ahead, in the middle of the clearing you see an injured rare fox")
        print("thats colored gold and red, do you help the fox, ignore it or take its fur for profit\n")

def choice_path4():
        choice = input("14. Help the fox" \
                       "15. Ignore the fox" \
                       "16. Take its fur for profit\n")
        
        
if choice == "14":
        print("You carefully approach the injured fox, it looks at you with pleading eyes, you reach into you bag to find some")
        print("bandages and medicine, luckily you packed extra supplies for your journey, you carefully bandage the fox's wounds")
        print("and give it some water, after a few minutes the fox gets up and  hands you what it looks like a small map, the")
        print("fox then runs off into the forest, you look at the map and see that it shows an X marking to a spot deeper in")
        print("the forest, you decide to follow the map, after a few hours of searching you reach the spot marked on the map, you")
        print("finnaly find the spot, you start digging and find a chest buried in the ground, you open the chest and find gold, jewels,")
        print("a cape, and a yellow gemstone!\n")
        print("Congratulations! You have found the Treasure of Autumn!\n")

def choice_path3():
  if choice == "12":
       forest_path()       
  elif choice == "13":
       treehouse_path()       
  else:
      print("Invalid choice. Please try again.\n")
      choice_path3()     


if choice == "15":
       print("You decide to ignore the fox and continue on your way, as you walk deeper into the forest, suddenly an tribe of")
       print("hostile natives ambush you, they overpower you and take all your supplies, leaving you stranded in the forest with")
       print("no food or water, after days of wandering you give up hope and succumb to starvation.\n")
       print("You have failed your quest.\n")
choice_path4()

if choice == "16":
        print("You see the foxes fur would be worth a ton of gold, you quickly grab your knife and skin the fox, you put the fur")
        print("in your bag and turn back towards the path, as you walk back, a gigantic tree falls beside you, and before you")
        print("could run, it crushes you.\n")
        print("You have failed your quest.\n")
        choice_path4()


def treehouse_path():  
       print("You decide that going to the treehouse village might have a better chance of finding the treasure, you make your")
       print("way towards the village, as you get closer you see that the village is bustling with activity, people are going")
       print("about their daily lives, you approach one of the villagers, they look at you like they've seen an alien, how ")
       print("should you talk to them?\n")
       choice = input("17. Try to communicate with gestures\n"  
                      "18. Attempt to speak their language\n" 
                      "19. Offer them a gift from your homeland\n")
       
       if choice ==   "17":
              return communication_path()
       elif choice == "18":
              return language_path()
       elif choice == "19":
              return gift_path()
       
def communication_path():
       print("You try to communicate with gestures, the villager looks confused but seems to understand you want to say, they"
             "Motion for you to follow them, they lead you to the village elder, the elder listens to your story and decides to"
             "help you, they give you a map with an X marking a spot deep in the nearby forest, you follow the map and after"
             "a few hours of searching you reach the spot marked on the map, you start digging and find a chest buried in the"
             "ground, inside you find gold, jewels, a cape, and a red gemstone!")
       print("Congratulations! You have found the Treasure of Autumn!\n")
       print("What direction should you go to next?")
       direction_path3()

def language_path():
       print("You attempt to speak their language, but you only manage to butcher a few words, the villager looks at you angrily\n"
            "and calls for others, soon you are surrounded by hostile villagers, they attack and kidnap you, you are held\n" 
            "captive for weeks before you manage to escape, but you are left with nothing but the clothes on your back, you\n"
            "eventually make your way back home dehydrated, starved, exhausted, and empty handed, you give up.\n")
print("You have failed your quest.\n")
choice_path3()

def gift_path():
       print("You offer the villager a gift from your homeland, they look at the gift curiously, after examining it they smile\n"
             "and motion for you to follow them, they lead you to their hut, they give you food and water, you explain your\n"
             "quest to them through gestures, they take you to the village elder, the villager explains your story to the\n"
             "elder, the elder decides to help you, they give you a map with an \"x\" marking a spot deep in the nearby forest,\n"
             "you follow the map and after a few hours of searching you reach the spot marked on the map, you start digging and\n"
             "find a chest buried in the ground, inside you find gold, jewels, a cape, and a red gemstone!\n")
       print("Congratulations! You have found the Treasure of Autumn!\n")
       print("What direction should you go to next?")
       direction_path3()

def direction_path3():
       direction = input("20. South (Treasure of Spring)\n"
                         "21. West  (Treasure of Summer)\n")
       
       if direction == "20":
              print("You set sail to the South!\n")
              return south_scene()
       elif direction == "21":          
                return west_scene()
       else:
                print("Invalid choice. Please try again.")
                direction_path3()


def south_scene():
       print("You decide that your next adventure will be the southern island, located directly south of your home, after a few")
       print("days of sailing you reach the island, you dock you ship and step onto the beautiful, sandy beach, you see palm trees")
       print("swaying in the warm breeze, beatiful lush greenery and exotic plants and animals you've never seen before, its like")
       print("a paradise, you explore the beautiful lush island, and you manage to build an temporary shelter of palm leaves and")
       print("wood. As night creeps over the island, you go to sleep, but you are then woken up by weird loud noises outside your")
       print("shelter, do you investigate the noises, or stay in your shelter?\n")
choice = input("22. Investigate the noises\n"
               "23. Stay in your shelter\n")



def investigate_path():
       print("Curiosity gets the better of you and you decide to investigate the noises, you muster up the courage and step"
      "outside your shelter, as you do, you are greeted by an unwelcomed guest of black tall creatures with glowing"
      "purple eyes, you are stuck in a trance-like state, unable to move, you can only watch as the the figures purple"
      "eyes get bigger and bigger, getting closer and closer, until you cant see no more.")
       print("You have failed your quest.\n")
       choice_path5()

def stay_path():
       print("You decide to stay in your shelter, hoping the noises will go away, they eventually get farther away, until they are gone you cautiously"
       "look outside your shelter, you see nothing but the night and stars, you go back to sleep, and awake to a beautiful sunny morning, you decide"
       "to explore more of the island, as you walk deeper into the island, you name some of the exotic plants and animals, and jot them down in your"
       "journal, after a few hours of exploring you reach a beautiful waterfall, and the stream flowing from it, you drink some out of the stream and"
       "feel refreshed, you see a cave entrance behind the waterfall, do you enter the cave or rest by the waterfall.")

def choice_path5():
       if choice == "22":
        return investigate_path()
if choice == "23":
       stay_path()
        
else:
       print("Invalid choice. Please try again.")
       choice_path5()

choice = input("24. Enter the cave\n"
               "25. Rest by the waterfall\n")

def choice_path6():
       if choice == "24":
              return cave_path()
       elif choice == "25":
              return waterfall_path()
       else:
              print("Invalid choice. Please try again.")
              choice_path6()

def cave_path():
       print("You are have heard stories of hidden treasures in caves behind waterfalls, so you decide to enter the cave, as you step inside bats"
       "fly past you, the cave is dark and damp, you walk deeper into the cave, after a few minutes you reach a large chamber with walls"
       "covered in colorful, glowing crystals, in the center you see a large glowing crystal with a treasure map inside it, you brought some tools"
       "with you for your journey, witch tool should you use to break the crystal?")

def choice_path7():
       choice = input("26. Hammer\n"
                      "27. Chisel\n"
                      "28. Pickaxe\n")
       return choice

if choice == "26":
       print("You use the hammer to try and break the crystal, you strike it with all your might, the crystal shatters into a million pieces, the" 
       "shards fly everywhere, one sharp shard stabs you in the chest, you fall to the ground, helpless, as you die of loss of blood.")
       print("You have failed your quest.\n")
       choice_path6()

if choice == "27":
       print("You carefully use the chisel to break the crystal, after a few hours of careful work, you manage to break the crystal without damaging"
         "the map inside, you unroll the map and see that it shows different landmarks on the island, with one landmark with an X marking, near"
         "the center of the island, you follow the map, after an hour of walking, you reach the spot marked on the map, when you get to the place,"
         "you see an entrance of an underground tunnel, you enter the tunnel, and find what it looks like a maze! You navigate through the maze using"
         "the direction on the back of the map, you eventually reach a room at the end of the maze, with three paths leading towards the left, right,"
         "and middle, which path do you take.")
       
choice = input("28. Left path\n"
               "29. Middle path\n"
               "30. Right path\n")

def choice_path8():
       if choice == "28":
              return left_path()
       elif choice == "29":
              return middle_path()
       elif choice == "30":
              return right_path()
       else:
              print("Invalid choice. Please try again.")
              choice_path8()

def left_path():
       print("You take the left path, after a few minutes of walking you reach a dead end, as you turn around to go back, you trigger a hidden trap,"
         " the floor opens beneath you, and you fall into a pit of spikes.")
print("You have failed your quest.\n")
choice_path8()

def middle_path():
       print("You take the middle path, as it seems most convincing, you walk for a few minutes and at the end of the path you see a lever on the wall,"
         " do you pull the lever or go back?")
choice = input("31. Pull the lever\n"
               "32. Go back\n")
def choice_path9():
       if choice == "31":
              return lever_path()
       elif choice == "32":
              return middle_path()
       else:
              print("Invalid choice. Please try again.")
              choice_path9()

def lever_path():
       print("You pull the lever, you hear a rumbling sound, the ceiling opens up then a large anvil falls from above, crushing you instantly.")
       print("You have failed your quest.\n")
choice_path9()

def right_path():
       print("You take the right path, the tunnel is long and narrow, after awhile, you hear echos of flowing water ahead, you walk faster and soon reach"
              " a large underground waterfall, with a sparkling pool below, you see a chest at the base of the waterfall, you swim to the chest and open it,"
              " inside you find gold, jewels, armor, and a pink gemstone!\n")
       
print("Congratulations! You have found the Treasure of Spring!\n")
print("Would you like to go to the final direction?")

def choice_path10():
  choice = input("33. Yes\n"
                 "34. No \n")
choice_path10()

def west_scene():
       print("You decide that your final adventure will be the western island (Or whatever the user ends on), located directly west of your home," \
       " after a few days of sailing you reach the island, you dock your ship and step onto the sandy desert, you see nothing but sand dunes and cacti" \
       " as far as the eye can see, the sun is blazing hot, you feel thirsty by just looking at the dry desert, you scan the desert for any signs of life," \
       " you see a rocky formation in the distance, you decide to head towards it, hoping to find some shade from the scorching sun, you make your way" \
       " towards the rocky formation, When you get there, you see its a large mesa, with a few desert trees and plants, around it, you take shelter" \
       " underneath one of the trees, you spot a group of arabs riding camels in the distance, you walk towards them, hoping they can help you, they" \
       " see you and stop their camels, you luckily speak a good amount of their language from your previous travels, you explain your quest to them," \
       " they say that they can help you but first you must give them something in return, what do you give them?")

choice = input("35. Gold from previous treasures\n"
               "36. Your compass\n"
               "3. Your weapons\n")

def choice_path11():
       if choice == "35":
              return gold_path()
       elif choice == "36":
              return compass_path()
       elif choice == "37":
              return weapons_path()
       else:
              print("Invalid choice. Please try again.")
              choice_path11()

def gold_path():
       print("You reach inside your backpack and hand them the gold from previous adventures, they nod in agreement and invite you to ride on one of" \
       " their camels, you hop on one, and they take you to an anceint temple, they tell you its filled with various traps and puzzles and no one has" \
       " ever dared to step inside. you thanked them and said goodbye and stepped inside the temple, the door closes from behind you, inside the temple"
       " is a stone with anceint arab words written on it, it reads, In the heat I stand both day and night, yet I never sweat, though the sun is bright," \
       " I point the way with shadows long~ guess my name and you prove strong, you take a minute to process the question, then come up with the anwser~")





if choice == "33":
       west_scene()
elif choice == "34":
              print("Really? After all this work you dont want to finish your quest? Oh well, home you go.")
              print("You have failed your quest.\n")
              choice_path10()         
else:
       print("Invalid choice. Please try again.")
       choice_path10()  

       
if choice == "28":
       print("You use the pickaxe to try and break the crystal, you strike it a little too hard, the crystal breaks in half, and so does the map"
         "inside, you are left with nothing but shattered glass and torn paper.")
print("You have failed your quest.\n")
choice_path7()












       
       






