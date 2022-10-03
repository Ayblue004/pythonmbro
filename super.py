def super_hero():
    x = input("Is your super hero a man?")
    if x == "no":
        print("Your super hero is Wonder woman")
    elif x == "yes":
        x = input("Can your hero fly?")
        if x == "no":
            print("your hero is Flash")
        elif x == "yes":
            x = input("Does your hero have hair")
            if x == "yes":
                print("your hero is superman")
            elif x == "no":
                print("your hero is vision")

super_hero()
