def introScene():
    print("Example")
    choice = input("Choose a, b, or c: ")
    if choice == "a":
        return scene1()
    elif choice == "b":
        return scene2()
    elif choice == "c": 
        return scene3()
    
    def scene1():
       print("Scene 1")

    def scene2():
       print("Scene 2")

    def scene3():
       print("Scene 3")

