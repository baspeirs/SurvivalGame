from sys import exit

def win():
    print("\nCongratulations! You have ignored the world and you live to fight another day! Have a snack!")
    exit(0) # this informs the user they have one then exits the program

def dead(why):
    print('\n', why, "You done messed up.")
    exit(0) # this is one way to loose and exit the program

def rick_roll():
    print("\nYou are surrouded by nothing but darkness and Rick Astly's \"Never Gonna Give You Up\"")
    print("You've been Rick Rolled and there is no point in going on. You're dead")
    exit(0) # The other way to loose and exit the program

def start():
    print("You're out for a stroll and you hear a very particular noise coming from a house in your neighborhood")
    print("Would you like to investigate?")

    choice_1 = input('\n>> yes or no\n>>')

    if choice_1 == 'yes':
        print("Okay, lets check it out")
        random_house()
        print(">>> work?")
    elif choice_1 == 'no':
        neighborhood()#-------------------> begin neighborhood function 
    else:
        print("Well, I cant just stand here!")
        start() # this will start the program over, we can wait till later to start the killing

def random_house():
    print("You walk up to the house and notice the door is ajar and you can see through the window\n How would you like to proceed?")
    llama_moved = False

    while True:
        
        choice_2 = input('\nopen door, or spy?\n>>')

        if choice_2 == 'open door' and llama_moved == False:
            dead("You walk in and a llama with a hat stabs you in chest 37 times.")
        elif choice_2 == 'open door' and llama_moved == True:
            print(""" You walk inside to investitgate, nothing appears to be wrong...
            But you notice a pamphlet on the table... its tickets for a cruise!!
            Would you like to take a ticket for yourself?""")

            take_ticket = input('\n>> ')

            if take_ticket == 'yes':
                print("Fuck it, why not go on a cuise?! You deserve some R&R")
                boat()
            elif take_ticket == 'no':#begins neighborhood function 
                print("Stealing is bad, lets just leave it there.")
                neighborhood()#----------------> start neighborhood function
            else:
                dead("You've been caught by the llama wearing a hat and he stabbs you 37 times in the chest")
        
        elif choice_2 == 'spy':
            print("In the window you see a llama wearing a hat... strange...")
            print("What would you like to do?")
            print("make noise, knock, or flee")

            choice_3 = input('\n>>')

            if choice_3 == 'make noise':# lets set llama_moved to true
                print("The llama becomes distracted from what it was doing and walks into the other room...\n The coast is clear")
                llama_moved = True
            elif choice_3 == 'knock':#does nothing
                print("You tap at the window and duck so you are not seen.. It is unclear if the distraction worked, but you must act now.")
            elif choice_3 == 'flee':#start neighborhood function 
                print("Yeah, this is kinda creepy, lets get out of here")
                neighborhood() # ------------------------> nighborhood function 
            else:
                print("Well, we cant just stand here all day, let's do something!")
        else:
            dead("That didn't work. A llama with a hat has decided you'd be the perfect speciman for his meat dragon.")

def boat():
    print("""Ahh yes, you have finally borded the ship and it is off to sea.
    But no cruise is complete without activities right?
    heres a list of the activities today!""")
    activities = ['fanta sea', 'pbj song', 'martial arts']
    
    print('\n', activities)
    act1 = input("Pick one! \n>>")

    if act1 == 'fanta sea':
        dead("""Four women preform a song. You dont quite understand the meaning but they keep singing about a soft drink
        The ask you if you "wanta fanta" but before you can respond, they force feed you a peach flavored soft drink...
        You were not prepared and you inhale most of the liquid and drown.""")
    
    elif act1 == 'pbj song':
        print("""Ahh yes, a real life banana plays the song of his people to the croud.
        The song is qute enjoyable and you now agree that it is peanut butter jelly time!
        
        The ship has stopped in a port in south america, would you like to visit the city?""")

        s_ameri = input('\n>> ')

    elif act1 == 'martial arts':
        print("Its Chuck norris and he is punching things with his chin fist! Quite entertaining!")
        print("The ship has stopped in a port in south america, would you like to visit the city?")

        s_ameri = input('\n>> ')
    else:
        print("thats not an option..")
        boat()
    
    if s_ameri == 'yes':
        print("okay, lets go!")
        trip() #-------------> insert trip function here
    else:
        print("Well, lets pick a new activity!")
        activities.append('llamas?')
        activities.append('musical preformance')
        print(activities)

        act2 = input("\n>> ")
    
    if act2 == 'llama':
        dead("""Yes, there were indeed two llamas aboard the ship.. and they were up to no good!
        The ship explodes and only one lifeboat is functional...
        The lifeboat was hyjacked by the two llamas and you are left to die!""")
    elif 'music' in act2:
        rick_roll()
    else:
        dead("""There were two llamas aboard the ship and they were up to no good!
        The ship explodes and only one lifeboat is functional...
        The lifeboat was hyjacked by the two llamas and you are left to die!""")

def trip():
    print("""You are wondering the streets of a wonderful South American city!
    The economy doesnt seem to be very wealthy but the culture is quite rich!
    However, you see two llamas and two unicorns consulting, then they split up...
    Would you like to follow either of them?""")

    follow = input('> unicorn\n> llama\n> other >> ')

    if 'unicorn' in follow:
        print("You follow the unicorns into the mountains of South America")
        candy_mountain()#------------->function for candy mountain goes here
    elif 'llama' in follow:
        dead("The llamas sir up a revolution in the city and you die amungst all the chaos")
    else:
        dead(f"{follow} was a bad choice. The city has broken into chaos and you're now dead... ")

def candy_mountain():
    print("You followed the unicorns up the hills to an oddly built structure labeled 'Candy Mountain'.")
    print("Would you like to follow them inside?")

    inside = input('\n>> ')

    if inside == 'yes':
        dead("You are hit upside the head and are barely concious when two unicorns remove your kidney...")
    else:
        dead("Well, anything is better than going inside this horribly built structure...As you move away from the area, you are shot in the knee by an arrow. Your adventuring days are over...")

def neighborhood():
    print("Its a beautiful sunny day, there is a guy in a neck brace mowing his lawn...")
    print("He appears to be having trouble.. He is flailing his arms and yelling things like 'fuck' and 'Bob Saget'...")
    print("Would you like to help him?")

    help = input('\n>> ')

    if 'yes' in help:
        dead('He was surrounded by a swarm of bees.. And you forgot your EpiPen.')
    else:
        print("Yeah, fuck that, did you see all those bees? lets just keep moving on...")
    
    print("There is a car on the road and a couple of dudes are jamming to what is probably a strait banger")
    print("Would you like to join?")

    join_1 = input('\n>>')

    if 'yes' in join_1:
        rick_roll()
    else:
        print("Those guys look like trouble. No thank you, lets keep moving.")
    
    print("Further down the road there is a lemonaid stand. Yummy! But there is a duck along the way.")
    print("You try to avoid the duck but he manages to stop you anyway and asks if you have any grapes..")

    grape_list = ['grapes']

    for grape in grape_list:
        print("\nDo you have any grapes?")

        grapes = input("\n>> ")

        if 'run' in grapes:
            print("Yeah, lets get the fuck up out of here!")
            break
        else:
            print(grape_list)
            grape_list.extend(grape_list)

            item = grape_list.count('grapes')

            if item >= 256:
                dead("Thats too many grapes!")

    print("Further down the road, there is an old video game! Its Zero Wing! Would you like to play?")

    play = input('\n>> ')

    if 'yes' in play:
        dead('It was a trap! Now all your base are belong to them!')
    else:
        print('Naw, fuck that. We want to keep our base.')

    print("You see a group of people.. They are plotting to run into a cave! Do you want to join?")

    join_2 = input('\n>> ')

    if 'yes' in join_2:
        dead('Mid plot, somone yells "LEEROY JENKINS" and runs into the cave causing everyone to die.')
    else:
        print("Naw, that Leeroy Jenkins kid is in that group. He always ruins shit")

    print("Holy shit! Its Chuck Norris! Do you wanna go get an autograph?")
    
    autograph = input('\n>> ')

    if 'yes' in autograph:
        dead("Chuck's aura was too powerful and your body criples from his presence.")
    else:
        print("Fuck Chuck Norris.. He should have given a thumbs down at that dogeball game.")
    
    print("Alas, you have made it home! Would you like to turn on the radio?")

    radio = input('\n>> ')

    if 'yes' in radio:
        rick_roll()
    else:
        print("Yeah, fuck that. Lets just relax.")
        #--------------> insert home function
        home()
        exit()

def home():
    print("Its been a long weird day... Would you like to check the mail or just ignore the world?")

    mail = input('\n>> ')
        
    if 'check' in mail:
        print("There's a free ticket for a cruise!! Would you like to go?")

        cruise = input('\n>> ')

        if cruise == 'yes':
            print("Hell yeah! Let's get to it!")
            boat()
        else:
            print("Yeah, that doesnt sound appeasing at all. Lets just relax here at home.")
            win()
    elif 'mail' in mail:
        print("There's a free ticket for a cruise!! Would you like to go?")

        cruise = input('\n>> ')

        if cruise == 'yes':
            print("Hell yeah! Let's get to it!")
            boat()
        else:
            print("Yeah, that doesnt sound appeasing at all. Lets just relax here at home.")
            win()
    else:
        print("Yeah, fuck the world today. Let's ignore it all and just rest.")
        win()




start()