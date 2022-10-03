convo_greet = ["hello","hi","how are you"]
convo_how = ["how old are you","how long have you been alive"]
convo_where = ["where are you", "where do you live"]
convo_going = ["bye", "see you later"]


def resp():
    greet = input("Hello or Hi me to wake me up")
    if greet in convo_greet:
        print("Hey!")
        how = input("Ask me a how question")
        if how in convo_how:
            print("I am a few hours old")
            where = input("Try to get me to tell you where I am") 
            if where in convo_where:
                print("I currently live on the cloud")
                bye = input("I'm a bit tired. can we call it a day?")
                if bye in convo_going:
                    print("Have a nice day :)")
                elif bye not in convo_going:
                    print("I'm sorry, I have to go now :(")
            elif where not in convo_where:
                print("I might not be able to give a correct answer")
        elif how not in convo_how:
            print("I'm sorry I don't have an answer to that question")
    elif greet not in convo_greet:
        print("Hnmmm :/")


resp()


    
