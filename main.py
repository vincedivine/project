yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]

def WelcomeUser():
  print ("Welcome to my text based adventure game. In this game you will be offered choices for different scenarios, if you choose the \ncorrect option you may move onto the next obstacle. If you choose incorrectly you may need to start over and try again.\n")

WelcomeUser()
    
# Intro into game
name = input("What is your name?\n")
print("Greetings, " + name + ". Let's go on this adventure!")
print("You find yourself outside of a Spooky looking Castle.")
print("Can you find your way through?\n")

# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the Castle?\nyes/no\n")
    if response == "yes":
        print("You head into the Castle. You hear the strong wind blowing in the distance.\n")
    elif response == "no":
        print("You are not ready for this adventure. Goodbye, " + name + ".")
        quit()
    else: 
        print("What was that?.\n")
 
# Second part of game
response = ""
while response not in directions:
    print("To your left, you see a Knight.")
    print("To your right, there is a long hallway.")
    print("There is a Castle wall directly in front of you.")
    print("Behind you is the Castle exit.\n")
    response = input("Which direction do you choose?\nleft/right/forward/backward\n")
    if response == "left":
        print("The Knight kills you. Farewell, " + name + ".")
        quit()
    elif response == "right":
        print("You head farther into the Castle.\n")
    elif response == "forward":
        print("You definitely can't climb up that wall.\n")
        response = "" 
    elif response == "backward":
        print("You leave the Castle. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")

# Third part of game
response = ""
while response not in directions:
    print("To your right, you see a monster.")
    print("To your left, there is an equally long hallway.")
    print("There is a spike covered wall directly in front of you.")
    print("Behind you is an open window with a way out.\n")
    response = input("Which direction do you choose?\nleft/right/forward/backward\n")
    if response == "right":
        print("The Monster eats you. Farewell, " + name + ".")
        quit()
    elif response == "left":
        print("You head farther into the Castle.\n")
    elif response == "forward":
        print("You die trying to climb the wall. Farewell, " + name + ".")
        quit()
        response = "" 
    elif response == "backward":
        print("You leave the Castle. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")

# Fourth part of game
response = ""
while response not in directions:
    print("To your right, you see a ferocius monster.")
    print("To your left, there is a dragon.")
    print("There is a large fire directly in front of you.")
    print("Behind you is an open window with a way out.\n")
    response = input("Which direction do you choose?\nleft/right/forward/backward\n")
    if response == "right":
        print("The Monster eats you. Farewell, " + name + ".")
        quit()
    elif response == "left":
        print("You choose to fight the dragon. You win and venture deep into the castle.\n")
    elif response == "forward":
        print("You die trying to go through the fire. Farewell, " + name + ".")
        quit()
        response = "" 
    elif response == "backward":
        print("You leave the Castle. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")

# Final part of game
response = ""
while response not in directions:
    print("To your left, you see a stream of lava.")
    print("To your right, you see the king, he is equipped for a battle.")
    print("There is another knight directly in front of you.")
    print("Behind you is an open window with a way out.\n")
    response = input("Which direction will you choose?\nleft/right/forward/backward\n")
    if response == "left":
        print("The Monster eats you. Farewell, " + name + ".")
        quit()
    elif response == "right":
        print("You choose to battle the king. You slowly approach him.\n") 
    elif response == "forward":
        print("You are killed trying to walk past the knight. Farewell, " + name + ".")
        quit()
        response = "" 
    elif response == "backward":
        print("You leave the Castle. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")

# The battle with the king
response = ""
while response not in directions:
    print("As you approach the king you come across a crate full of weapons,Do you choose a bow?")
    print("Do you choose a banana?")
    print("Do you choose a sword?")
    print("Do you choose to use your hands?\n")
    response = input("Which weapon do you choose?\nbow/banana/sword/hands\n")
    if response == "bow":
        print("The bow does not come equipped with arrows. You are killed by the king, Farewell, " + name + ".")
        quit()
    elif response == "sword":
        print("You use the sword to defeat the king, you win " + name + ".")
        quit()
    elif response == "banana":
        print("A banana would never work. You lose, Farwell" + name + ".")
        quit()
        response = "" 
    elif response == "hands":
        print("Using your hands is just as useless as the banana. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")
