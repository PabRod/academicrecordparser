def papers(data):
    data = data.query('Type == "Paper"')
    data = data[["Date", "Name", "Author", "Publisher"]]
    return data