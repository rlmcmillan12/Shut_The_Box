
from funct import shut_the_box_roll, master_list_total, master_list_cover, clear_console, cover_checker
from banners import page_header, you_win, you_lose

master_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while True:

    print(page_header)
    main_menu_choice = input(
        "To play a game press 1\nTo read the instructions press 2\n To quit the game press q\nPlease make a choice: "
    )
    if main_menu_choice != "1" and main_menu_choice != "2":
        print("Please enter a valid entry...")
    elif main_menu_choice == "2":
        print(
            """
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
    - 4 & 3 & 1"""
        )
    elif main_menu_choice.lower() == "q":
        exit()
    elif main_menu_choice == "1":
        while True:
            clear_console()
            start_turn = input("LETS TAKE A ROLL!\nPress ENTER to roll: ")
            if start_turn != "":
                print("Thats not the ENTER key!")
            if start_turn == "":
                close_total = 0
                del_list = []
                print(master_list)
                roll_total = shut_the_box_roll(master_list)
                ml_total = master_list_total(master_list)
                valid_moves = cover_checker(roll_total, master_list)

                if roll_total < ml_total and valid_moves == True:
                    clear_console()
                    print("Your total roll is: " + str(roll_total))
                    print("\nYou have " + str(master_list) + " open")
                    while close_total < roll_total:
                        print(
                            "You have " +
                            str((roll_total - close_total)) + " left to close"
                        )
                        close = int(
                            input("Which number would you like to close?: ")
                        )
                        for num in master_list:
                            if close == num:
                                close_total += num
                                del_list.append(close)
                            if close not in master_list:
                                print("That is not open")
                            else:
                                print("Try Again!")
                        master_list_cover(master_list, del_list)
                    clear_console()
                    del del_list
                    print(master_list)

                elif roll_total == ml_total:
                    clear_console()
                    print("You rolled: " + str(roll_total) + "\n")
                    print(you_win)
                    end_game = input(
                        "\nPress ENTER to restart the game: ")
                    if end_game == "":
                        del del_list
                        master_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                        break
                    else:
                        break

                else:
                    clear_console()
                    print("You rolled: " + str(roll_total) + "\n")
                    print(you_lose)
                    end_game = input(
                        "\nPress ENTER to restart the game: ")
                    if end_game == "":
                        del del_list
                        master_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                        break
                    else:
                        del del_list
                        master_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                        break
