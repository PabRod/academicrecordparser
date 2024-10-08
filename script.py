from academicrecordparser.io import *
from academicrecordparser.filters import *
from academicrecordparser.auxs import *

slugs = ["publications", "teaching", "education", "sci-comm"]
langs = ["en", "es", "nl"]
output_dir = "../../content/pages/"

template_args = as_template_args(get_data())
environment = Environment(loader=FileSystemLoader("templates/"))

for slug in slugs:
    for lang in langs:
        use_template(slug, lang, output_dir, environment, **template_args)