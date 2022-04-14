from random import randint
import os
# from main import master_list


def clear_console():
    os.system('clear')


def one_die():
    roll_total = randint(1, 6)
    return roll_total


def two_dice():
    roll_total = randint(2, 12)
    return roll_total


def shut_the_box_roll(master_list):
    if 7 not in master_list and 8 not in master_list and 9 not in master_list:
        roll_choice = input(
            "would you like to roll one or two dice?\nEnter 1 or 2: ")
        if roll_choice == "1":
            return one_die()
        elif roll_choice == "2":
            return two_dice()
        else:
            return shut_the_box_roll(master_list)
    elif 7 in master_list or 8 in master_list or 9 in master_list:
        print("You still have 7, 8, and 9 uncovered\nRolling two dice")
        return two_dice()


def master_list_total(master_list):
    master_total = 0
    for i in master_list:
        if i != " ":
            master_total += int(i)
    return master_total


def master_list_cover(master_list, del_list):
    for num in del_list:
        master_list[num - 1] = " "


def cover_checker_list_maker(master_list):
    cover_checker_list = []
    for i in master_list:
        if i != " ":
            cover_checker_list.append(i)
    return cover_checker_list


def cover_checker(roll_total: int, master_list: list[int], memo={}):
    filtered_list = cover_checker_list_maker(master_list)
    if (roll_total in memo):
        return memo[roll_total]
    if (roll_total < 0):
        return False
    if (roll_total == 0):
        return True

    for i in range(len(filtered_list)):
        if cover_checker(roll_total - filtered_list[i], filtered_list[i + 1:], memo):
            memo[roll_total] = True
            return True

    memo[roll_total] = False
    return False
