# Scott Mobarry
# INST 326

"""
This is how you run these tests:
python -m pylint videogamessales.py
"""

import pytest
import pandas
from videogamessales import make_games_clean, videogames_more_like_this, videogames_filtering, videogames_sampling, suggest_games
 
def startup():
    """
    A common set of values for these tests.
    """
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
    return (my_df, my_titles, my_platforms, my_age, num_suggestions)


def test_videogames_more_like_this():
    """
    Testing the happy path for the more like this.
    """
    (my_df, my_titles, my_platforms, my_age, num_suggestions) = startup()
    found_genres = videogames_more_like_this(my_df, my_titles)
    assert set(found_genres) == set(["Racing", "Action"])


def test_videogames_filtering():
    """
    Testing the happy path.
    """
    (my_df, my_titles, my_platforms, my_age, num_suggestions) = startup()
    found_genres = pandas.Series(["Racing", "Action"])
    df_can_suggest = videogames_filtering(my_df, found_genres, my_platforms, my_age, my_titles)
    assert set(df_can_suggest['Name'].to_list()) == set(['Game E', 'Game F'])


def test_videogames_sampling():
    """
    Testing the happy path. Because the sampling was random the random state needed to be set to a constant.
    """
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
    """
    It tests calling the three sub methods all at once.
    """
    (my_df, my_titles, my_platforms, my_age, num_suggestions) = startup()
    sugestions = suggest_games(
        my_df,
        my_titles,
        my_platforms,
        my_age,
        num_suggestions,
        )
    assert set(sugestions) ==  set(['Game E', 'Game F'])
