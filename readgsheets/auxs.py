def clickable_link(name, url):
    """ Turn name + url into a markdown clickable link """
    return "[" + name + "](" + url + ")" # Formatted strings seem to cause problems with pandas