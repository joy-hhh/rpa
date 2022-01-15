from docxtpl import DocxTemplate
import pandas as pd

doc = DocxTemplate('note.docx')
fiscal_year = {
    'cur_year' : 2021,
    'prior_year' : 2020
}

# Load note data from excel file
note_data = pd.read_excel("values.xlsx")

# Create context dictionary from note data file
context = dict(zip(note_data['var'], note_data["value"]))

for key in context:
    if context[key] < 0:
        context[key] = format(context[key], ',d').replace('-','(') + ")"
    elif context[key] > 0:
        context[key] = format(context[key], ',d')
    else: 
        context[key] = '-'

context.update(fiscal_year)
doc.render(context)
doc.save("note_output.docx")