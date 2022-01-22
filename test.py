import sys


def check_input(usrinput):  # first function
    if usrinput < 0:
        print("Please type positive number.")
        sys.exit()
    elif usrinput == 0:
        print("You don't have any cat. That's sad :-(")
        sys.exit()

              
def cats_info(numcats):  # second function
    try:
        ch_input = int(numcats)
        check_input(ch_input)
        if ch_input >= 4:
            print("You have a lot of cats.")
        else:
            print("That's not that many cats.")
    except ValueError:
        print("Write a number.")
    

print("How many cats do you own?")
usr_cats = input()
cats_info(usr_cats)
