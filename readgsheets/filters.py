# For publications page
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

# For teaching page
def teaching(data):
    data = data.query('Type == "Course" & (Role == "Professor") | (Role == "Teaching assistant")')
    data = data[["Date", "Name", "Institution", "Country"]]
    return data

# For education page
def formal(data):
    data = data.query('Type == "Regular_studies"')
    data = data[["Date", "Name", "End.date", "Institution", "Country"]]
    return data

def secondments(data):
    data = data.query('Type == "Secondment"')
    data = data[["Date", "End.date", "Institution", "Country"]]
    return data

def conferences(data):
    data = data.query('Type == "Congress" | Type == "Workshop"')
    data = data[["Date", "Name", "Institution", "Role", "Country"]]
    return data