# Docs: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_gbq.html
# Installation
#   pip install pandas-gbq

# Import the libraries
import pandas_gbq
import pandas as pd

# Set destination of table to be written, 
# with form dataset.tablename.
table_id = "playground.pd_test_write_bq"

# Set GCP Project ID
project_id = "elmo-gcp"

# Dictate whether to 'fail', 'replace' or 'append' 
# if the destination table already exists.
method = 'replace'

# Create a DataFrame
# Note: You must verify that the structure and data types
# in the DataFrame match the schema of the destination table
df = pd.DataFrame(
    {
        "my_string" : ["a", "b", "c"],
        "my_int"    : [1, 2, 3],
        "my_float"  : [1.0, 2.0, 3.0],
        "my_bool"   : [True, False, False],
    }
)

# Write a DataFrame to a Google BigQuery table
pandas_gbq.to_gbq(
    dataframe=df, 
    destination_table=table_id, 
    project_id=project_id, 
    if_exists=method
)

# Display the result
print("Successfully written data to {}".format(table_id))
