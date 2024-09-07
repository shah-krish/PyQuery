from google.cloud import bigquery

def connect_to_database():
    client = bigquery.Client()
    return client