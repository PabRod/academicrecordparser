import pandas as pd
from tabulate import tabulate
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from readgsheets.filters import *

# ===== Input =====
def get_data():
    """ Typical workflow """ 
    return drop_clutter(enrich(parse()))

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

def as_template_args(data):
    template_args = {"publications_table" : as_table(papers(data)), 
                     "num_publications" : papers(data).shape[0],
                     "books_table" : as_table(books(data)),
                     "thesis_table" : as_table(thesis(data)),
                     "teaching_table" : as_table(teaching(data)),
                     "num_teaching" : teaching(data).shape[0],
                     "formal_table" : as_table(formal(data)),
                     "secondments_table" : as_table(secondments(data)),
                     "conferences_table" : as_table(conferences(data)),
                     "num_conferences" : conferences(data).shape[0],
                     "talks_table" : as_table(talks(data)),
                     "num_talks" : talks(data).shape[0],
                     "blogs_en_table" : as_table(blogs(data, language="English")),
                     "num_blogs_en" : blogs(data, language="English").shape[0],
                     "blogs_es_table" : as_table(blogs(data, language="Spanish")),
                     "num_blogs_es" : blogs(data, language="Spanish").shape[0],
                     "blogs_nl_table" : as_table(blogs(data, language="Dutch")),
                     "num_blogs_nl" : blogs(data, language="Dutch").shape[0],
                     "others_table" : as_table(others(data)),
                     }
    
    return template_args

# ===== Output =====
def as_table(data):
    """ Export as a table """
    return tabulate(data,
                    tablefmt="github",
                    headers="keys", 
                    showindex=False)

def use_template(slug, lang, output_dir, environment=Environment(loader=FileSystemLoader("templates/")), **template_args):
    """ Turn dictionary data into document via a jinja template """
    ## Load the template
    template = environment.get_template(f"{slug}.jinja")

    ## Create the content
    content = template.render(lang = lang, **template_args) # Pass all args but lang as dictionary

    ## Save it
    filename = Path(output_dir, f"{slug}-test-{lang}.md")
    with open(filename, mode = "w") as f:
        f.write(content)