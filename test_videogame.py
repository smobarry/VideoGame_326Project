#Happy path
#inputs and expected outputs are "normal"
#Edge cases ("unhappy path")
#inputs are unusual or special values
#may trigger exceptions

import pytest
from videogamestest import get_user_age_from_name
#games = list(csv.DictReader(open("video games project - games.csv")))
#users = list(csv.DictReader(open("video games project - users.csv")))
#ownedgames = list(csv.DictReader(open("video games project - ownedgames.csv")))

users = [
        {'id': 1, 'Name': 'Alice', 'Age': 16},
        {'id': 6, 'Name': 'Clark', 'Age': 13},
    ]
    
def test_1():
    # Test got a record by name
    
    name = 'Alice'
    age = get_user_age_from_name(users, name)
    assert age == 16
    
    # Test got a age for record 


#def test age_limit by giving it edge cases

def test_funcname(self, parameter_list):
    """
    docstring
    """
    raise NotImplementedError