from pandas import isna
from numpy import vectorize
from pycountry import countries

@vectorize
def clickable_link(name, url):
    """ Turn name + url into a markdown clickable link """
    if isna(url):
        return name
    else:
        return f"[{name}]({url})"

@vectorize
def countryname_as_flag(countryname):
    if isna(countryname):
        return countryname
    else:
        return countries.get(name = countryname).flag