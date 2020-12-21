# Docs: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_gbq.html
# Installation
#   pip install pandas-gbq

import pandas_gbq
import pandas as pd

table_id = "[DATASET].[TABLE]"

project_id = ""

# Note: You must verify that the structure and data types
# in the DataFrame match the schema of the destination table
schema = {
    "my_string" : ["a", "b", "c"],
    "my_int"    : [1, 2, 3],
    "my_float"  : [1.0, 2.0, 3.0],
    "my_bool"   : [True, False, False],
}

df = pd.DataFrame(schema)

print("Writing dataframe to '{}'...".format(table_id))
pandas_gbq.to_gbq(
    dataframe=df, 
    destination_table=table_id, 
    project_id=project_id, 
    if_exists="replace"
)