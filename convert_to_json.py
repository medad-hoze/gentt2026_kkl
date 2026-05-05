import pandas as pd
import json

xls = pd.ExcelFile('תכולות_ממג_2026.xlsx')

# Option 1: All sheets into one JSON file (dict of sheet_name -> records)
all_data = {}
for sheet in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet)
    # Replace NaN with None so JSON gets null instead of NaN
    df = df.where(pd.notnull(df), None)
    all_data[sheet] = df.to_dict(orient='records')

with open('data_2026.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2, default=str)

