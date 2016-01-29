def getMenuOption(prompt, options):
    goodOption = False
    while not goodOption:
        option = raw_input(prompt)
        if option.lower() in options:
            goodOption = True
        else:
            print "Please make a valid selection from the menu."
    return option.lower()
    
def menu():
    print "------Epic Pong Menu-------"
    print "| 1) Human vs Human     |"
    print "| 2) Human vs Computer  |"
    print "| 3) Options            |"
    print "| Q) Quit               |"
    print "-------------------------"
    optionsList = ["1",
                   "2",
                   "3",
                   "Human vs Human ",
                   "Human vs Computer",
                   "Options",
                   "up down up down left right left right b a start",
                   "Quit",
                   "Q"]
    return getMenuOption("> ", optionsList)
    
menu()

