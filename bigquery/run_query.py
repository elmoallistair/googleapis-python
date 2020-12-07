# Import librariey
from google.cloud import bigquery

# Initialize a BigQuery client
bigquery_client = bigquery.Client()

# Construct a SQL query
query = """
    SELECT
      CONCAT(
        'https://stackoverflow.com/questions/',
        CAST(id as STRING)) as url,
      view_count
    FROM `bigquery-public-data.stackoverflow.posts_questions`
    WHERE tags like '%google%'
    ORDER BY view_count DESC
    LIMIT 10
"""

# Run a SQL query
print("Executing job...")
query_job = bigquery_client.query(query)

# Get the result
results = query_job.result()

# Displaying the query result
print("Result")
for row in results:
    print("{} : {} views".format(row.url, row.view_count))
