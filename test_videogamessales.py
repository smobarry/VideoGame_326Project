# Happy path
# inputs and expected outputs are "normal"
# Edge cases ("unhappy path")
# inputs are unusual or special values
# may trigger exceptions

import pytest
import pandas
from videogamessales import make_games_clean, videogames_more_like_this, videogames_filtering, videogames_sampling, suggest_games
 
def startup():

    my_df = pandas.DataFrame({
        "Name": ["Game A", "Game B", "Game C", "Game D", "Game E", "Game F"],
        "Platform": ["XB", "Wii", "XB", "PS", "XB", "PS"],
        "Genre": ["Racing", "Sports", "Shooter", "Action", "Action", "Racing"],
        "Rating": ["E", "E", "M", "T", "T", "E"],
    })        

    my_titles = [
        'Game A',
        'Game D',
        'Game X',
        'Game Y']
    my_platforms = ['XB', 'PS']
    my_age = 16
    num_suggestions = 2

    if False:
        the_suggestions = suggest_games(
            my_df,
            my_titles,
            my_platforms,
            my_age,
            num_suggestions,
            )
        print(f'{len(the_suggestions)} suggestions = {the_suggestions}')
    return (my_df, my_titles, my_platforms, my_age, num_suggestions)


def test_videogames_more_like_this():
    (my_df, my_titles, my_platforms, my_age, num_suggestions) = startup()
    print('----- test_videogames_more_like_this +++++')
    print(f'my_df = {my_df}')
    found_genres: pandas.Series = videogames_more_like_this(my_df, my_titles)
    print(f'found_genres ={found_genres}')
    assert set(found_genres) == set(["Racing", "Action"])


def test_videogames_filtering():
    (my_df, my_titles, my_platforms, my_age, num_suggestions) = startup()
    found_genres = pandas.Series(["Racing", "Action"])
    df_can_suggest = videogames_filtering(my_df, found_genres, my_platforms, my_age, my_titles)
    assert set(df_can_suggest['Name'].to_list()) == set(['Game E', 'Game F'])


def test_videogames_sampling():
    df_can_suggest = pandas.DataFrame({
        "Name": ["Game A", "Game B", "Game C", "Game D", "Game E", "Game F"],
        "Platform": ["XB", "Wii", "XB", "PS", "XB", "PS"],
        "Genre": ["Racing", "Sports", "Shooter", "Action", "Action", "Racing"],
        "Rating": ["E", "E", "M", "T", "T", "E"],
    })
    num_suggestions = 2
    suggestions = videogames_sampling(df_can_suggest, num_suggestions, random_state=1)
    assert set(suggestions) == set(['Game B', 'Game C'])

def test_suggest_games():
    (my_df, my_titles, my_platforms, my_age, num_suggestions) = startup()
    sugestions = suggest_games(
        my_df,
        my_titles,
        my_platforms,
        my_age,
        num_suggestions,
        )
    assert set(sugestions) ==  set(['Game E', 'Game F'])
