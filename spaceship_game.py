#Gregory Clarke
#Computer Programming
#10/12/2017


POINTS=0
PLANET=""

def menu(): #Starting Menu.
    global NAME
    NAME=input("What is your name?: ")
    print("Hello "+NAME+", your mission is to fly from planet to planet.")
    print("1 = Start Game")
    print("2 = Enter Planet Code")
    print("3 = Exit Game")
    choice=input("Choice: ")
    if choice=="1":
        print("Welcome")
        print("You are on Earth")
        takeoff()
    elif choice=="2":
        global planet_code
        planet_code=input("What plant code would you like to enter?: ").lower()
    
        if planet_code=="1":
            print("Welcome")
            print("You are on Earth")
            takeoff()
            
        if planet_code=="2":
            print("Welcome")
            print("You are on Mercury")
            takeoff()
        if planet_code=="3":
            print("Welcome")
            print("You are on Venus")
            takeoff()
        if planet_code=="4":
            print("Welcome")
            print("You are on Mars")
            takeoff()
        if planet_code=="5":
            print("Welcome")
            print("You are on Jupiter")
            takeoff()
        if planet_code=="6":
            print("Welcome")
            print("You are on Saturn")
            takeoff()
        if planet_code=="7":
            print("Welcome")
            print("You are on Uranus")
            takeoff()
        if planet_code=="8":
            print("Welcome")
            print("You are on Neptune")
            takeoff()
                
    elif choice=="3":
        quit()
    else:
        print("Invalid option")
        menu()
    
def escape_velocity(takeoff,escapevelocity): #The ship's statistics such as speed
    global POINTS
    speed2=float(input("What is your ship's speed in miles per hour?: "))
    if speed2>escapevelocity*1.1:
        print("Your speed is to fast and you crashed. You had "+POINTS+"")
        
        POINTS=0
        startup()

    elif speed2<escapevelocity*0.9:
        print("Your speed is to slow and you crashed")
        POINTS=0
        startup()
    else:
        print("YOU MADE IT. You have gained 5 points.")
        POINTS=POINTS+5
        print("You now have "+POINTS+"")
        
        continue_()
        
def continue_():
    print("1 = Continue")
    print("2 = Exit Game")
    continue1=input("Would you like to continue?: ")
        
    if continue1=="1":
        takeoff()
    elif continue1=="2":
        exit()
    else:
        print("Invalid Option. Choose again.")
        continue_
            
def takeoff(): # The planet choices. If the input is known, it will move to the escape_velocity module. If the input is unknown, it will restart the module. 
    global planet_codeS
    print("Mercury")
    print("Venus")
    print("Earth")
    print("Mars")
    print("Jupiter")
    print("Saturn")
    print("Uranus")
    print("Neptune")

    destination1=input("Where would you like to go?: ").lower()
    global PLANET
    PLANET=destination1


    if PLANET=="earth":
        planetcode=2
        print("Welcome to Earth. Your Planet Code is "+str(planetcode)+".")
        escapevelocity=25022.3694
        escape_velocity(takeoff,escapevelocity)

    elif PLANET=="mercury":
        planetcode=2
        print("Welcome to Mercury. Your Planet Code is "+str(planetcode)+".")
        escapevelocity=9506.979
        escape_velocity(takeoff,escapevelocity)
    elif PLANET=="venus":
        planetcode=3
        print("Welcome to Venus. Your Planet Code is "+str(planetcode)+".")
        escapevelocity=23174.66
        escape_velocity(takeoff,escapevelocity)
    elif PLANET=="mars":
        planetcode=4
        print("Welcome to Mars. Your Planet Code is "+str(planetcode)+".")
        escapevelocity=11251.79
        escape_velocity(takeoff,escapevelocity)
    elif PLANET=="jupiter":
        planetcode=5
        print("Welcome to Jupiter. Your Planet Code is "+str(planetcode)+".")
        escapevelocity=134663.6
        escape_velocity(takeoff,escapevelocity)
    elif PLANET=="saturn":
        planetcode=6
        print("Welcome to Saturn. Your Planet Code is "+str(planetcode)+".")
        escapevelocity=80731.031
        escape_velocity(takeoff,escapevelocity)
    elif PLANET=="uranus":
        planetcode=7
        print("Welcome to Uranus. Your Planet Code is "+str(planetcode)+".")
        escapevelocity=47825.698
        escape_velocity(takeoff,escapevelocity)
    elif PLANET=="neptune":
        planetcode=8
        print("Welcome to Neptune. Your Planet Code is "+str(planetcode)+".")
        escapevelocity=52702.219
        escape_velocity(takeoff,escapevelocity)
    else:
        print("Invalid Option, check list and spelling")
        takeoff()
             
menu()   








    
 

    

    
