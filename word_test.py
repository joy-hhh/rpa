# conda install -c conda-forge docxtpl
# Load library
from docxtpl import DocxTemplate
import jinja2
import pandas as pd

# Load Template from financials , add context for cy and py, and render
doc = DocxTemplate('note.docx')
context = {
    'cur_year' : 2021,
    'prior_year' : 2020
}
doc.render(context)
doc.save("note_output.docx")


# Load note data from excel file
note_data = pd.read_excel("values.xlsx")

# Create context dictionary from note data file
context = dict(zip(note_data['var'], note_data["value"]))

# Create ouput with full updated context
doc = DocxTemplate('note.docx')
doc.render(context)
doc.save("note_output.docx")


# Add custom filter to convert items to numbers with commas
def comma(value):
    return "{:,}".format(value)
jinja_env = jinja2.Environment()
jinja_env.filters['c'] = comma


# Create updated output with full updated context
doc = DocxTemplate("note.docx")
doc.render(context, jinja_env)
doc.save("note_output.docx")

