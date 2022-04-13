print(
    """
_____________        _____     _____________            ________              
__  ___/__  /_____  ___  /_    ___  __/__  /______      ___  __ )_________  __
_____ \__  __ \  / / /  __/    __  /  __  __ \  _ \     __  __  |  __ \_  |/_/
____/ /_  / / / /_/ // /_      _  /   _  / / /  __/     _  /_/ // /_/ /_>  <  
/____/ /_/ /_/\__,_/ \__/      /_/    /_/ /_/\___/      /_____/ \____//_/|_|  
"""
)

master_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


main_menu_choice = input("To play a game press 1\nTo read the instructions press 2\nPlease make a choice: ")

if main_menu_choice == "1":

elif main_menu_choice == "2":
    print("""
A round consists of a player repeatedly throwing the dice until he or she cannot continue. 
Each throw of the dice is taken as follows:

    If 7, 8 and 9 are all covered, the player decides whether to throw one die or two.
    If any of these 3 numbers are still uncovered, the player must use both dice.

The player throws the die or dice into the box and adds up the die or dice. 
The player must then cover available numbers that add up to the total thrown. 
So for instance, if the total is 8, the player may choose one of the following options:
    - 8
    - 7 & 1
    - 6 & 2
    - 5 & 3
    - 5 & 2 & 1
    - 4 & 3 & 1""")
else:
    print("Please enter a valid entry...")
