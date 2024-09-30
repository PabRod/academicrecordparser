import pandas as pd

def _default_key():
    """ Return the default key """
    with open("key.txt") as f:
        key = f.readline()
        
        return(key)

def parse(key=_default_key()):
    """ Return the raw data """
    link = f"https://docs.google.com/spreadsheets/export?id={key}&format=csv"
    data = pd.read_csv(link)

    return data