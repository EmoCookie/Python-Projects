import time

name = input("Enter your name: ")
print("Welcome",name,"! It is an honour to make your acquaintance!")

answer = input("You are on a mystical adventure! Your path is a dirt road. Do you wish to proceed the left or right side of the road? ").lower()

if (answer == "left"):
    q2 = input("You have reached a cave.\nDo you wish to enter? Insert 'yes' or 'no'. ").lower()
    if (q2 == "yes"):
        print("You have met your demise! The dragon burnt you into ashes when you stumbled over a rock and awakened it!")
    elif (q2 == "no"):
        print("You continued walking on the same direction until you realised you've been circling the same area.\nYou are now stuck in a loop hole!")
    else:
        print("Invalid option! You got taken away by an eagle!")   

elif (answer == "right"):
    q3 = input("After walking for several hours you have found a door.\nHowever, it was not attached to any building but stood there as though it was waiting for you to open it.\nDo you wish to open the door or walk away?\nEnter 'door' to open the door or 'walk' to leave. ").lower()
    if (q3 == "door"):
        print("Congratulations! You have found the land to the mystical creatures of WarGround!\nThey greet you with open arms and invited you to their party! ")
        print("You walk to the party and towards the stage where you were crowned as their special guest.")
        time.sleep(5)
        print("'Thank you Warrior!', said the Queen.")
        
        dots = "...."
        for i in range(0,len(dots)):
            print(dots[i], end="")
            time.sleep(2)

        print("Your sacrifice as our meal means a great deal to us.")

    elif (q3 == "walk"):
        print("You walked even longer and eventually collapsed. You woke up only to find back at your home! Congratulations! You survived!")
    else:
        print("Invalid option! You got taken away by an eagle!")

else:
    ("Invalid option! Game is terminated!")