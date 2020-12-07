# Docs: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_gbq.html
# Installation
#   pip install pandas-gbq

# Import library
import pandas as pd

# Set GCP Project ID
project_id = "elmo-gcp"

# Construct a SQL query
query = """
    SELECT name
    FROM `bigquery-public-data.usa_names.usa_1910_current`
    WHERE state = 'TX'
    LIMIT 100
"""

# Load data from Google BigQuery.
df = pd.read_gbq(
    query=query, 
    project_id=project_id,
    dialect='standard' 
)

# Display the result
print("Successfully read data from BigQuery !")
print(df)
