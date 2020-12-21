#Scott Mobarry
#Salah Waji
#Directory ID: smobarry
#INST 326

"""
In this module the video game sales data is used to provide a suggestion for
video games that a user might want to buy.

We downloaded a pre-scraped csv file from:
https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings

Documentation for how to use pandas start at:
https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

For more documentation use this website:
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
    The method make_games_clean() creates a dataframe from the cleaned video games data file.
    This throws away data we can't use.
    We downloaded the video games sales csv file from Kaggle
    and checked it into GitHub in the same directory as this script.
    The input csv file needs at least these 4 columns: ['Name', 'Platform', 'Genre', 'Rating']

    Args:
        fname (str): File name of csv file.
    Returns:
        mydf (pandas.DataFrame): the cleaned video games data.

    (Written by Scott Mobarry)
    Driver: Scott Mobarry
    Navigator: Salah Waji
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


def videogames_more_like_this(mydf, my_titles):
    """
    The videogames_more_like_this() method returns the genres the user likes.

    Args:
        mydf (pandas.DataFrame): the cleaned video games data.
        my_titles (list of str): the titles that the user has played and liked
            but not to be suggested.

    Returns:
        found_genres (list of str): the found genres in games that the user likes.

    (Written by Scott Mobarry)
    Driver: Scott Mobarry
    Navigator: Salah Waji
    """
    mydf_found_games = mydf[mydf['Name'].isin(my_titles)]
    # games found in the database from the titles that were given from the user.
    #print(f'mydf_found_games = {mydf_found_games}')
    #found_titles = mydf_found_games['Name'].value_counts()
    #found_platforms = mydf_found_games['Platform'].value_counts()
    found_genres = mydf_found_games['Genre'].value_counts().index.tolist()
    #found the genres in the dataset of games the user liked.
    #found_ratings = mydf_found_games['Rating'].value_counts()
    #print(f'found_titles = {found_titles}')
    #print(f'found_platforms = {found_platforms}')
    #print(f'found_genres = {found_genres}')
    #print(f'found_ratings = {found_ratings}')
    return found_genres


def videogames_filtering(mydf, found_genres, my_platforms, my_age, my_titles):
    """
    This method filters the video game data frame rows by this criteria:
    1. Only keep genres of games the user likes.
    2. Only keep platforms the user wants.
    3. Only keep the ratings the user can buy due to their age restrictions.
    4. Don't keep the titles the user gave they already like.

    Args:
        mydf (pandas.DataFrame): the cleaned video games data.
        found_genres (list of str): the found genres in games that the user likes.
        my_platforms (list of str): the list of interesting platforms available
            in the dataset.
        my_age (int): the age of the user in years.
        my_titles (list of str): the list of video game titles not to be
            considered in the suggester.

    Returns:
        df_can_suggest (pandas.DataFrame): the subset of videogames that can be
            suggested to the user.

    (Written by Scott Mobarry)
    Driver: Scott Mobarry
    Navigator: Salah Waji
    """
    my_ratings = [ rating for rating in
                ESRB_MIN_AGE if
                ESRB_MIN_AGE[rating] <= my_age]
    # These are the ratings that the user can buy for their age.
    #print(f'my_ratings = {my_ratings}')
    #print(f'head of mydf_games = {mydf.head()}')
    #print(f'describe Ratings = {mydf['Rating'].describe()}')
    #print(f'value_counts = {mydf['Rating'].value_counts()}')
    df_can_suggest = mydf[
        (~ mydf['Name'].isin(my_titles))
        & mydf['Genre'].isin(found_genres)
        & mydf['Platform'].isin(my_platforms)
        & mydf['Rating'].isin(my_ratings)
        ]
    return df_can_suggest


def videogames_sampling(df_can_suggest, num_suggestions, random_state=None):
    """
    This method samples the games that survived the filtering.
    We now choose a few video game titles to suggest.

    Args:
        df_can_suggest (pandas.DataFrame): the subset of videogames that can be
            suggested to the user.
        num_suggestions (int): the number of suggestions displayed to the user.
        random_state (int): Leave set to None except for unit test.
    Returns:
        list of str: the suggestions of titles for the GUI.

    (Written by Scott Mobarry)
    Driver: Scott Mobarry
    Navigator: Salah Waji
    """

    # print(f'df_can_suggest.count() = {df_can_suggest.count()}')
    print(f'df_can_suggest = \n{df_can_suggest}')
    #df_suggestions = df_can_suggest.head(num_suggestions)
    df_suggestions = df_can_suggest.sample(n = num_suggestions, random_state=random_state)
    # The next statement extracts a python list of suggested titles
    suggestions = df_suggestions['Name'].tolist()
    return suggestions


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

    Args:
        mydf (pandas.DataFrame): the cleaned video games data.
        my_titles (list of str): the titles of video games that the user has
            played and liked but not to be suggested.
        my_platforms (list of str): the list of interesting platforms available
            in the dataset.
        my_age (int): the age of the user in years.
        num_suggestions (int): the number of suggestions displayed to the user.

    Returns:
        list of str: the game titles that are suggested to the user.

    (Written by Scott Mobarry)
    Driver: Scott Mobarry
    Navigator: Salah Waji
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

    found_genres = videogames_more_like_this(mydf, my_titles)

    df_can_suggest = videogames_filtering(mydf, found_genres, my_platforms, my_age, my_titles)

    suggestions = videogames_sampling(df_can_suggest, num_suggestions)

    return suggestions


if __name__ == '__main__':
    # This is an example useage via the command line.

    the_df = make_games_clean('Video_Games_Sales_as_at_22_Dec_2016.csv')

    the_titles = [
        'Star Wars: Battlefront',
        'Madden NFL 06',
        'STORM: Frontline Nation',
        'Men in Black II: Alien Escape']
    the_platforms = ['XB', 'PS']
    the_age = 16
    the_num_suggestions = 10

    the_suggestions = suggest_games(
        the_df,
        the_titles,
        the_platforms,
        the_age,
        the_num_suggestions,
        )
    print(f'{len(the_suggestions)} suggestions = {the_suggestions}')
