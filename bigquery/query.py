# Run a SQL Query

from google.cloud import bigquery

bigquery_client = bigquery.Client()

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

print("Executing job...")
query_job = bigquery_client.query(query)

print("\nResult:")
results = query_job.result()
for row in results:
    print("{} : {} views".format(row.url, row.view_count))
