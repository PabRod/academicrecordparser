import pandas as pd
from tabulate import tabulate

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

def enrich(data):
    """ Enrich table with extra columns """
    from readgsheets.auxs import clickable_link

    data["Name"] = data["Name"].where(pd.isna(data["URL"]), 
                                         clickable_link(data["Name"], data["URL"]))
    
    return data

def drop_clutter(data):
    """ First round of removing unnecessary data """
    TO_BE_DROPPED = ["Peer.reviewed", 
                    "ECTS",
                    "Pay.day",
                    "Amount",
                    "Grades",
                    "Notes"]
    
    return data.drop(columns = TO_BE_DROPPED)

def as_table(data):
    """ Export as a table """
    return tabulate(data,
                    tablefmt="github",
                    headers="keys", 
                    showindex=False)