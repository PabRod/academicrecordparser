def papers(data):
    data = data.query('Type == "Paper"')
    data = data[["Date", "NameURL", "Author", "Status", "Publisher"]]
    return data