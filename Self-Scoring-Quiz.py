score = 0

print("What is the color of the sea?")
print("A. Red")
print("B. Yellow")
print("C. Blue")
print("D. None of the above")

anwser = input("Choose A, B, C, or D: ")
if anwser == "C":
    print("Correct!")
    score = score + 1
     
else: 
    print("Incorrect.")
    score = score - 1
       


print("What is the best chocolate? (2 extra points for right anwser)")
print("A. Reeses")
print("B. Milky way")
print("C. Pistacio chocolate")
print("D. Dove")

anwser = input("Choose wisely")
if anwser == "D":
    print("Very good")
    score = score + 2

else:
    print("Wrong")
    score = score - 1

print("What is the best soda?")
print("A. Squirt")
print("B. Coka Cola")
print("C. Dr. Pepper")
print("D. Sprite")

anwser = input("Which one is best?")
if anwser == "A":
    print("I agree")
    score = score + 1
    
else:
    print("wrong")
    score = score - 1
         

print("What is the best time of year?(10 extra points for right anwser)")
print("A. Winter")
print("B. Summer")
print("C. Fall")
print("D. Spring")

anwser = input("Choose correctly")
if anwser == "B":
 print("Well done.")
 score = score + 10

else:
    print("Womp womp")
    score = score - 1


print("Congrats! You have completed the quiz :)")
print("Here is your score")
print(score)

                
             
                
