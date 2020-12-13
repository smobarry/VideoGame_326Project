# Scott Mobarry
# Directory ID: smobarry
# INST 326

# We download a pre-scraped csv file from https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings



import pandas as pd

# To get the minimum age for each ESRB rating use this website https://en.wikipedia.org/wiki/Entertainment_Software_Rating_Board
esrb_min_age = {'E': 4, 'T': 13, 'M': 17, 'E10+': 10, 'EC': 2, 'K-A': 6, 'RP': 18, 'A0': 18}

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

def make_games_clean():
    """
    Creates a dataframe with games data.
    We downloaded the csv file from Kaggle and checked it into GitHub in the same directory as this script.  
    """
    fname = 'Video_Games_Sales_as_at_22_Dec_2016.csv'
    df = pd.read_csv(fname)
    #print(f'df.head() = {df.head(10)}')
    #print(df_games_all.describe())
    df = df[['Name', 'Platform', 'Genre', 'Rating']]
    # We kept only the columns that we wanted. Indexing using a list means the list of four columns to keep from the 16 original columns.
    #print(f'df.head() = {df.head(10)}')
    rows_to_keep = df['Rating'].notna()
    # print(f'rows_to_keep = {rows_to_keep}')
    df = df[rows_to_keep]
    # We just removed all rows with NaN as the rating. The remaining rows all have ratings.
    #print(f'df.head() = {df.head(10)}')
    #print(f'df.tail() = {df.tail(10)}')
    return df


def suggest_games(
    df,
    my_titles,
    my_platforms,
    my_age,
    num_suggestions,
    ):

    #avail_titles = df['Name'].value_counts()
    avail_platforms = df['Platform'].value_counts()
    avail_genres = df['Genre'].value_counts()
    avail_ratings = df['Rating'].value_counts()
    # print(f'avail_titles = {avail_titles}')
    print(f'avail_platforms = {avail_platforms}')
    print(f'avail_genres = {avail_genres}')
    print(f'avail_ratings = {avail_ratings}')

    my_ratings = [ rating for rating in esrb_min_age if esrb_min_age[rating] <= my_age]
    # print(f'my_titles = {my_titles}')
    print(f'my_ratings = {my_ratings}')
    # print(f'my_platforms = {my_platforms}')
    # print(f'head of df_games = {df_games_set.head()}')
    # print(f'describe Ratings = {df_games_set.Rating.describe()}')
    # print(f'value_counts = {df_games_set.Rating.value_counts()}')

    df_found_games = df[df['Name'].isin(my_titles)]
    # print(f'df_found_games = {df_found_games}')

    #found_titles = df_found_games['Name'].value_counts()
    found_platforms = df_found_games['Platform'].value_counts()
    found_genres = df_found_games['Genre'].value_counts()
    print(type(found_genres.index))
    found_ratings = df_found_games['Rating'].value_counts()
    # print(f'found_titles = {found_titles}')
    print(f'found_platforms = {found_platforms}')
    print(f'found_genres = {found_genres}')
    print(f'found_ratings = {found_ratings}')

    df_suggest = df[
        (~ df['Name'].isin(my_titles))
        & df['Genre'].isin(found_genres.index.tolist())
        & df['Platform'].isin(my_platforms)
        & df['Rating'].isin(my_ratings)
        ]
    #print(f'df_suggest.count() = {df_suggest.count()}')
    df_suggestions = df_suggest.head(num_suggestions)
    suggestions = df_suggestions['Name'].tolist()

    print(f'df_suggest = {df_suggest}')
    # print(f'df_suggest = {df_suggest.set_index("Name")}')
    print(f'df_suggestions = {df_suggestions.set_index("Name")}')
    # print(f'type(df_suggest) = {type(df_suggest)}')
    # print(f'type(df_suggest["Name"]) = {type(df_suggest["Name"])}')
    # df_suggest.set_index('Name', inplace=True)
    return suggestions


if __name__ == '__main__':

    df = make_games_clean()

    my_titles=['Star Wars: Battlefront', 'Madden NFL 06', 'STORM: Frontline Nation', 'Men in Black II: Alien Escape']
    my_platforms = ['XB', 'PS']
    my_age = 16
    num_suggestions = 10

    suggestions = suggest_games(
        df,
        my_titles,
        my_platforms,
        my_age,
        num_suggestions,
        )
    print(f'{len(suggestions)} suggestions = {suggestions}')
