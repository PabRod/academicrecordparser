from pandas import isna
from numpy import vectorize
from pycountry import countries

def clickable_link(name, url):
    """ Turn name + url into a markdown clickable link """
    return "[" + name + "](" + url + ")" # Formatted strings seem to cause problems with pandas

@vectorize
def countryname_as_flag(countryname, width=30, height=20):
    if isna(countryname):
        return countryname
    else:
        return countries.get(name = countryname).flag