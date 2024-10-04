def papers(data):
    data = data.query('Type == "Paper"')
    data = data[["Date", "Name", "Author", "Publisher"]]
    return data

def books(data):
    data = data.query('Type == "Book"')
    data = data[["Date", "Name", "Role", "Institution"]]
    return data

def thesis(data):
    data = data.query('Type == "Thesis"')
    data = data[["Date", "Name", "Role", "Institution"]]
    return data