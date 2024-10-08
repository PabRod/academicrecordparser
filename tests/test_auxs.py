from academicrecordparser.auxs import *

def test_clickable_link():
    expected = '[My website](https://pabrod.github.io)'
    assert(expected == clickable_link("My website", "https://pabrod.github.io"))