def madlib():
    place = input("Enter any place: ")
    verb = input("Enter a verb : ")
    noun = input("Enter a noun that denotes people: ")


    Madlib_game = f"When a lion was resting in the {place}, a mouse began racing up and down his body for amusement.\
    The lion’s sleep was interrupted, and he awoke enraged. The lion was going to {verb} the mouse when the mouse begged him to let him go. \
    “I assure you, if you save me, I will be of immense help to you in the future.” "+ "The lion laughed at the mouse’s self-assurance and freed him.\
    A group of {} arrived in the forest one day and captured the lion.".format(noun)+ "They had him tied to a tree.\
    The lion began to roar as he struggled to get out. Soon, the mouse passed by and spotted the lion in distress. \
    He dashed off, biting on the ropes to free the lion, and the two hurried off into the woods." 

    print(Madlib_game)