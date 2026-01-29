 while True:
        choice = input("Type in your choice (A, B, C): ").lower()

        print("\n")

        if choice == "a":
            return scene0A()
        elif choice == "b":
            return scene0B
        elif choice == "c":
            return scene0C
        else:
            print("Invalid choice. Please enter a, b, or c.")


def scene0A():
    # SCENE 0A: RED MECH

    inventory.append({
        "mech": "red"
    })

    print(
        "===\n"
        "\n"
@@ -54,7 +67,7 @@ def scene0A():
    )

    input("Press Enter to deploy...\n")
    return scene1()
    return hq()



@@ -63,6 +76,10 @@ def scene0A():
def scene0B():
    # SCENE 0B: BLUE MECH

    inventory.append({
        "mech": "blue"
    })

    print(        
        "===\n"
        "\n"
@@ -75,7 +92,7 @@ def scene0B():
    )

    input("Press Enter to deploy...\n")
    return scene1()
    return hq()



@@ -84,6 +101,10 @@ def scene0B():
def scene0C():
    # SCENE 0C: GRAY MECH

    inventory.append({
        "mech": "gray"
    })

    print(
        "===\n"
        "\n"
@@ -98,13 +119,13 @@ def scene0C():
    )

    input("Press Enter to deploy...\n")
    return scene1()
    return hq()





def scene1():
def hq():
     # SCENE 1: LEVIATHAN OUTPOST (HUB)

    print(
@@ -126,6 +147,21 @@ def scene1():
        "D) Outside the Outpost (Deploy to other zones)\n"
    )

    while True:
        choice = input("Choose destionation (a, b, c, d): ").lower()

        print("\n")

        if choice == "a":
            return admiral_office()
        elif choice == "b":
            return mechanics_bay()
        elif choice =="c":
            return bunk()
        elif choice == "d":
            outside_outpost()
        else:
            print("Invalid choice. Please enter a, b, c or d.")



@@ -143,7 +179,7 @@ def admiral_office():
    )

    input("Press Enter to return to Leviathan Outpost...\n")
    return scene1()
    return hq()



@@ -159,7 +195,7 @@ def mechanics_bay():
    )

    input("Press Enter to return to Leviathan Outpost...\n")
    return scene1()
    return hq()



@@ -174,7 +210,7 @@ def bunk():
    )

    input("Press Enter to return to Leviathan Outpost...\n")
    return scene1()
    return hq()



@@ -190,7 +226,7 @@ def outside_outpost():
    )

    input("Press Enter to return to Leviathan Outpost...\n")
    return scene1()
    return hq()