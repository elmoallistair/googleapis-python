# Docs: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_gbq.html
# Installation
#   pip install pandas-gbq

import pandas as pd

project_id = ""

query = """
    SELECT name
    FROM `bigquery-public-data.usa_names.usa_1910_current`
    WHERE state = 'TX'
    LIMIT 100
"""

print("Reading data from BigQuery...")
df = pd.read_gbq(
    query=query, 
    project_id=project_id,
    dialect='standard' 
)

print("\nResult:")
print(df)
