# Note this is only for terminal use. The HTML, CSS, JS codes are for website.

import sys
import random

print("\n\n\n********** Welcome to Taifun Wirbel! This is a randomizer for the card deck. Please read rules before using software **********")

def rndm():
    items_advantage = [
        "\nBlew Foreward:\n---\nYou have been blown foreward, move up two steps. Tell the group your favorite country\n",
        "\nTeleport:\n---\nMove up to the nearest player in front of you. If you are the first player move up ३ steps\n",
        "\nNitrous:\n---\nYou received a sudden boost of gas, move up 2 steps\n",
        "\nPushed foreward:\n---\nAnother person escaping the Taifun rammed you, giving a speed boost, move up 1 step\n",
        "\nMuffler Malfunction:\n---\nThe muffler is blasting air giving you a push forward, go up one step\n",
        "\nERS:\n---\nYou receive a sudden boost of energy. Tell the group your favorite car brand, then move up one step\n",
        "\nDRS:\n---\nYou recieved a two boost energy pack. Keep this in mind as you can use this anytime you want!\n",
        "\nBalloon Vendor:\n---\nYou saw a balloon vendor with a panda balloon. You buy it and attach it to your roof. You suddenly take flight, move up two steps\n",
        "\nOut of Creativity:\n---\nThe dev ran out of ideas, move up one step\n",
        "\ntreeeeeeeeee:\n---\nA tree crashed behind you giving you a boost, move up one step\n",
        "\nRobin Hood:\n---\nYou were given a friendly push by a random guy, move up one step\n"
    ]

    items_disadvantage = [
        "\nBlew back:\n---\nYou have been blown back, move back two steps\n",
        "\nTeleport²:\n---\nMove back to the nearest player behind of you. If you are the last player move back 3 steps\n",
        "\nNitrous²:\n---\nYou received a sudden boost of gas, unfortunately, it came out the front, must be a malfunction. Go back one step\n",
        "\nRammed off:\n---\nAnother person escaping the Taifun pulled a 'George Russel' and rammed you off the mountain, move down a row\n",
        "\nBumper down:\n---\nThe bumper broke, forcing you to fix it. Since you lost time, move back two steps\n",
        "\nICE CREAM!!!:\n---\nYou saw an irregular ice cream vendor who has your favorite ice cream. Tell the group your favorite ice cream flavor, then move back one steps for the time you lost\n",
        "\nFriendly Neighbor:\n---\nYou saw your neighbor with his engine broken down. You stop to help them. Move back one step for the time you lost\n",
        "\nBalloon Vendor²:\n---\nYou saw a(nother) balloon vendor. You attach the balloon to your roof, unfortunately, you took flight backwards, move back 2 steps\n",
        "\nSmushed like an ant:\n---\nYour car got smashed by a tree. Looks like you got to make the journey by feet. Move half the amount you roll, and if it is a one you dont move! If its an odd number, round the decimal down\n",
        "\nOut of Creativity²:\n---\nThe dev ran out of ideas, go back a step\n",
        "\nMasked Bandit:\n---\nYou were robbed of your nitrous by the masked bandit. Nitrous doesn't work on you anymore\n"
    ]

    while True:
        userchoice = input("\nEnter... \n1 for advantage, \n2 for disadvantage, \nq to quit: \n[dont cheat 😀]\n\n")

        if userchoice.lower() not in ["1", "2", "q"]:
            print("You MUST enter 1, 2, or q.")
            continue
        else:
            break
    
    if userchoice.lower() == "q":
        print("\n🎉🎉🎉🎉")
        print("Thank you for using randomiser\nDeveloped by Adi Momin\n")
        sys.exit("Bye! 👋")

    user = int(userchoice)

    if user == 1:
        card = random.choice(items_advantage)
        print(card)
    else:
        card = random.choice(items_disadvantage)
        print(card)

    return rndm()

rndm()
