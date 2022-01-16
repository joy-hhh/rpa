from docxtpl import DocxTemplate
import jinja2
import pandas as pd
import numpy as np

doc = DocxTemplate('note.docx')

# Load note data from excel file

val = pd.read_excel("values.xlsx")

# Create context dictionary from note data file
context ={}
for i in list(val.columns):
    for j in range(len(val[i])): 
        if np.isnan(val[i][j]):
            continue
        else: 
            context[i+str(j)] = val[i][j]


for key in context:
    if context[key] < 0:
        context[key] = format(int(context[key]), ',d').replace('-','(') + ")"
    elif context[key] > 0:
        context[key] = format(int(context[key]), ',d')
    else: 
        context[key] = '-'

fiscal_year = {
    'cur_year' : "2021",
    'prior_year' : "2020"
}
context.update(fiscal_year)

exrate = {
    'exrate' : "1,185.5"
}

context.update(exrate)

doc.render(context)
doc.save("note_output.docx")