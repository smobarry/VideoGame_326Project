"""
Names:
Scott Mobarry
Chidima Ibezimako
Salahdin Waji
Germain Biyao
Assignment: Final Project Proposal
INST 326
"""

import csv
import string


games = csv.reader(open("video games project - games.csv"))
for game in games:
    print(repr(game))
    
def console_v5():
    """ Creates an object containing the terminal inputs of the user as attributes of the object
    
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
def age_limit(age, ESRB_rat,):
    """
    This function will check for the age limit and give a a game based on 
    the rating. 
    Args:
        age(int)
        ESRB(str)
    """   
    if (age >= 17) and (ESRB_rat == 'M'):
        print("You can play games You can play games with an ESRB rating of M, T, and E.")
    elif ( age >= 13 & age < 17  ) and (ERSB_rat == 'T'):
        print ("You can play games with an ESRB rating of T and E.")
    elif(age >= 6 & age < 13) and (ESRB_rat == 'E'):
        print("You can only play games with an ESRB rating of E.")
        
def main():
    print ("please enter your age ")
    age = int(input("Enter age : "))