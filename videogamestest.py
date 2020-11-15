"""
Names:
Scott Mobarry
Chidima Ibezimako
Salahdin Waji
Germain Biyao
Assignment: Final Project Check In 1
INST 326
"""

import csv
import string

def inputdata():
    """
    (Scott) I created three csv files for the past game store data that will
    be used to tailor game recommendations. This will be ussed to recommend games of the 
    same genre as the user has bought in the past.
    Later we will fill filter down games they can actually own due to their
    age and game console type they own.
    """
    games = csv.reader(open("video games project - games.csv"))
    users = csv.reader(open("video games project - users.csv"))
    ownedgames = csv.reader(open("video games project - ownedgames.csv"))
 
    for game in games:
        print(repr(game))
    
    for user in users:
        print(repr(user))
 
    for purchase in ownedgames:
        print(repr(purchase))

    return games, users, ownedgames

def console_v5():
    """ (Chidima) Creates an object containing the terminal inputs of the user as attributes of the object
    
    Args:
       None
    
    Side effects:
       Prints out the type of game console chosen by the user, either Xbox or PlayStation
    """
    parser = argparse.ArgumentParser()
 
    parser.add_argument('console', choices=['Xbox', 'PlayStation'],
                        help="user must choose between one of the two consoles")
 
    args = parser.parse_args()
    c = args.console
 
    if c == 'Xbox':
        print(f'Gaming console entered is {args.console}')
    elif c == 'PlayStation':
        print(f'Gaming console entered is {args.console}')


"""
(Germain) This script will be limiting age of potential players
"""
#this method will ask the user to enter his age 
def age_limitcheck(age, ESRB_rat,):
    """
    This function will check for the age limit of the user and approve the game based on 
    the ESRB rating. 
    Args:
        age(int)
        ESRB(str)
    """
    oktobuy = False
    if (age >= 17) and (ESRB_rat in {'E', 'T', 'M'}):
        print("You can play games You can play games with an ESRB rating of E,T,M.")
        oktobuy = True
    elif ( age >= 13) and (ERSB_rat in {'E', 'T'}):
        print ("You can play games with an ESRB rating of E, T.")
        oktobuy = True
    elif(age >= 6) and (ESRB_rat == 'E'):
        print("You can only play games with an ESRB rating of E.")
        oktobuy = True
    return oktobuy
        
def main():
    print ("please enter your age ")
    age = int(input("Enter age : "))