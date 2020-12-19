"""
Scott Mobarry
Directory ID: smobarry
INST 326

We downloaded a pre-scraped csv file from
https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings

Documentation for how to use pandas start at
https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

For more documentation use this website
https://pandas.pydata.org/docs/reference/frame.html
"""

import pandas as pd

# To get the minimum age for each ESRB rating use this website
# https://en.wikipedia.org/wiki/Entertainment_Software_Rating_Board

ESRB_MIN_AGE = {'E': 4, 'T': 13, 'M': 17, 'E10+': 10, 'EC': 2, 'K-A': 6, 'RP': 18, 'A0': 18}
# This is a pandas dictionary of minimum ages for each rating in the dataset

"""
E       3991
T       2961
M       1563
E10+    1420
EC         8
K-A        3
RP         3
AO         1
"""

def make_games_clean(fname):
    """
    The method make_games_clean(fname) creates a dataframe from the cleaned video games data file.
    This throws away data we can't use.
    We downloaded the video games sales csv file from Kaggle
    and checked it into GitHub in the same directory as this script.
    The input csv file needs at least these 4 columns: ['Name', 'Platform', 'Genre', 'Rating']
    The inputs and outputs are stated below:
    input: file name of csv file
    output: Pandas dataframe with the cleaned video games data
    (Written by Scott Mobarry)
    """

    mydf = pd.read_csv(fname)
    #print(f'mydf.head() = {mydf.head(10)}')
    #print(mydf.describe())
    #print(mydf.info())
    mydf = mydf[['Name', 'Platform', 'Genre', 'Rating']]
    # We kept only the columns that we wanted.
    # Indexing using a list means the list of four columns to keep from the 16 original columns.
    #print(f'mydf.head() = {mydf.head(10)}')
    rows_to_keep = mydf['Rating'].notna()
    #print(f'rows_to_keep = {rows_to_keep}')
    mydf = mydf[rows_to_keep]
    #print(mydf.info())
    # I just removed all rows with NaN as the rating. The remaining rows all have ratings.
    #print(f'mydf.head() = {mydf.head(10)}')
    #print(f'mydf.tail() = {mydf.tail(10)}')
    return mydf


def suggest_games(
    mydf,
    my_titles,
    my_platforms,
    my_age,
    num_suggestions,
    ):
    """
    The method suggest_games() implements a video game suggestor that returns reccomendations
    to the user based off of the established criteria.
    The inputs and outputs for this method are stated below:

    inputs:
    The pandas dataframe of known games(mydf),
    the list of strings containing titles that the user owns and has played and liked,
    the gaming console platform the user wants a game for,
    the age of the intended user,
    the amount of video game suggestions the user would like.

    outputs:
    A list of game titles suggested to the user.
    (Written by Scott Mobarry)
    """
    # the value counts method is like GroupBy but simpler.
    # It groupby's the columns giving the counts.
    #avail_titles = mydf['Name'].value_counts()
    #avail_platforms = mydf['Platform'].value_counts()
    #avail_genres = mydf['Genre'].value_counts()
    #avail_ratings = mydf['Rating'].value_counts()
    #print(f'avail_titles = \n{avail_titles}')
    #print(f'avail_platforms = \n{avail_platforms}')
    #print(f'avail_genres = \n{avail_genres}')
    #print(f'avail_ratings = \n{avail_ratings}')

    my_ratings = [ rating for rating in
                ESRB_MIN_AGE if
                ESRB_MIN_AGE[rating] <= my_age]
    # These are the ratings that the user can buy for their age.
    #print(f'my_ratings = {my_ratings}')
    #print(f'head of mydf_games = {mydf.head()}')
    #print(f'describe Ratings = {mydf['Rating'].describe()}')
    #print(f'value_counts = {mydf['Rating'].value_counts()}')

    ## More Like This
    mydf_found_games = mydf[mydf['Name'].isin(my_titles)]
    # games found in the database from the titles that were given from the user.
    #print(f'mydf_found_games = {mydf_found_games}')
    #found_titles = mydf_found_games['Name'].value_counts()
    #found_platforms = mydf_found_games['Platform'].value_counts()
    found_genres = mydf_found_games['Genre'].value_counts()
    #found the genres in the dataset of games the user liked.
    #found_ratings = mydf_found_games['Rating'].value_counts()
    #print(f'found_titles = {found_titles}')
    #print(f'found_platforms = {found_platforms}')
    #print(f'found_genres = {found_genres}')
    #print(f'found_ratings = {found_ratings}')

    ## FILTERING
    df_can_suggest = mydf[
        (~ mydf['Name'].isin(my_titles))
        & mydf['Genre'].isin(found_genres.index.tolist())
        & mydf['Platform'].isin(my_platforms)
        & mydf['Rating'].isin(my_ratings)
        ]
    # The video game suggestor will filter rows by this criteria:
    # 1. Only keep genres of games the user likes
    # 2. Only keep platforms the user wants
    # 3. Only keep the ratings the user can buy due to their age restrictions
    # 4. Don't keep the titles the user gave they already like


    ## Sampling
    # of the games that survived the filtering we now choose a few to suggest
    # print(f'df_can_suggest.count() = {df_can_suggest.count()}')
    print(f'df_can_suggest = \n{df_can_suggest}')
    #df_suggestions = df_can_suggest.head(num_suggestions)
    df_suggestions = df_can_suggest.sample(n = num_suggestions)
    # The next statement extracts a python list of suggested titles
    suggestions = df_suggestions['Name'].tolist()
    #converts the suggestions into a python list of titles for the GUI
    return suggestions


if __name__ == '__main__':
    #this is an example useage via the command line
    fname = 'Video_Games_Sales_as_at_22_Dec_2016.csv'
    mydf = make_games_clean(fname)

    my_titles = [
        'Star Wars: Battlefront',
        'Madden NFL 06',
        'STORM: Frontline Nation',
        'Men in Black II: Alien Escape']
    my_platforms = ['XB', 'PS']
    my_age = 16
    num_suggestions = 10

    suggestions = suggest_games(
        mydf,
        my_titles,
        my_platforms,
        my_age,
        num_suggestions,
        )
    print(f'{len(suggestions)} suggestions = {suggestions}')
