



def user_information():
    """ (Salah)Prompts user for inforamtions and passes it to the recommendation method
    
    
        Returns:
            A dictionary of users information
            

        Side effects: 
            appends the games a user has (of the same genre) into a list
        
    """
    
    name = input("What is your name? ")
    
    age = input("Hello How old are you? ")
    
    preferred_genre= input("What genre of game do you like? ")
    owned_games_list = []
    #ask for games owned for the particular genre, so that we don't recommend a game he/she already owns
    console =input("What console do you use? ")
    
    response = input(str(" Do you have any games for that genre? y/n "))
    response.lower()
    if response == "y":
        owned_games = input(str("what games do you have for that genre " ))
        owned_games_list.append(owned_games)
    
    user_info = {"name": name, "Console": console, "age: ": age, "Preferred genre: " : preferred_genre, "games owned": owned_games_list}
    
    
    recommend_games(user_info)





def recommend_games(user_info):
    
   
    for values in user_info:
        for keys in user_info:
        #if user_info[1] <= 17:
            print(values, keys, sep=",")
    
    """if (age >= 17) and (ESRB_rat in {'E', 'T', 'M'}):
        print("You can play games You can play games with an ESRB rating of E,T,M.")
        oktobuy = True
    elif ( age >= 13) and (ERSB_rat in {'E', 'T'}):
        print ("You can play games with an ESRB rating of E, T.")
        oktobuy = True
    elif(age >= 6) and (ESRB_rat == 'E'):
        print("You can only play games with an ESRB rating of E.")
        oktobuy = True    
    """




if __name__ == "__main__":
    
    user_information()