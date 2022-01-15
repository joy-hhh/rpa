from docxtpl import DocxTemplate
import pandas as pd
import numpy as np

doc = DocxTemplate('note.docx')
fiscal_year = {
    'cur_year' : 2021,
    'prior_year' : 2020
}

# Load note data from excel file
val = pd.read_excel("values.xlsx")
note_data ={}
for i in list(val.columns):
    for j in range(len(val[i])): 
        if np.isnan(val[i][j]):
            continue
        else: 
            note_data[i+str(j)] = val[i][j]

# Create context dictionary from note data file
context = dict(zip(note_data['var'], note_data["value"]))
exrate = {
    'exrate' : 1185.5
}
context.update(exrate)

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