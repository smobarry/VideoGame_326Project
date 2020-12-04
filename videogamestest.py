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
import random
import pandas as pd

def inputdata():
    """
    (Scott) I created three csv files for the past game store data that will
    be used to tailor game recommendations. This will be used to recommend games of the 
    same genre as the user has bought in the past.
    Later we will fill filter down games they can actually own due to their
    age and game console type they own.
    """
    gametest = pd.read_csv("video games project - games.csv")
    gametest.set_index('id', inplace=True) 
    print(gametest)
    
    games = list(csv.DictReader(open("video games project - games.csv")))
    #print(games)
    
    df_users = pd.read_csv("video games project - users.csv")
    df_users.set_index('id', inplace=True) 
    print(df_users)
    
    users = list(csv.DictReader(open("video games project - users.csv")))
    #print(users)
    
    ownedgamestest = pd.read_csv("video games project - ownedgames.csv")
    print(ownedgamestest)
    
    ownedgames = list(csv.DictReader(open("video games project - ownedgames.csv")))
    return games, users, ownedgames, df_users

def console_v5():
    """ 
    (Chidima)
    Creates an object containing the terminal inputs of the user as attributes of the object
    
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


def get_userid_from_name(users, name):
    """
    From the name we will get a User id
    """
    byname = {}
    for d in users:
        n = d['Name']
        byname[n] = d
    user = byname[name]
    return user['id']

def get_userid_from_name_df(userstest, name):
    """
    From the name we will get a User id
    """
    return userstest[userstest.Name == name]



def get_user_age_from_userid(users, userid):
    """
    From the user id we will get an age.
    I created a dictionary to find the right user records.
    """
    byid = {}
    for d in users:
        n = d['id']
        byid[n] = d
    user = byid[userid]
    return user['Age']

def get_games_from_userid(owned, userid):
    """
    From the name we will get the games bought by this person
    """
    games = []
    for d in owned:
        n = d['User_id']
        if n == userid:
            games.append(d['Game_id'])
    return games

def get_genres_from_games(games, their_games):
    """
    From the games we will get the same genres
    """
    genres = set()
    for d in games:
        n = d['id']
        if n in their_games:
            genres.add(d['Genre'])
    return genres
    

def age_limitcheck(age, ESRB_rat,):
    """
    This script will be limiting age of potential players
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
    games, users, owned_games, df_users = inputdata()
    name = input("Please enter your name : ")
    
    their_userid = get_userid_from_name(users, name)
    their_age = get_user_age_from_userid(users, their_userid)
    df_userid = get_userid_from_name_df(df_users, name)
    
 
    their_games = get_games_from_userid(owned_games, their_userid)
    their_genres = get_genres_from_games(games, their_games)
    print(repr(their_userid))
    print(df_userid)
    print(repr(their_age))
    print(repr(their_games))
    print(repr(their_genres))
    
    for game in games:
        print(repr(game))
    
    for user in users:
        print(repr(user))
 
    for purchase in owned_games:
        print(repr(purchase))

    #(Scott)
    # from the name we will get an age (done)
    # from the name we will find a genre bought by this person(done)
    # from the genre we will find a list of possible games to recommend
    # from the age of the person we will only keep the games we can recommend 
    # we will display the recommendation
#UTA max

#df = pandas.DataFrame(holder)
#Exported to a csv for later use
#df.to_csv('shoe_dict_exported.csv', index = False )




if __name__ == "__main__":
    main()    