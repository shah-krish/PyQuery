import snowflake.connector

def connect_to_database():
    return snowflake.connector.connect(
        user="root",
        password="krish123",
        account="your_account_identifier",  # Replace with your Snowflake account identifier
        warehouse="your_warehouse",         # Optional: specify your warehouse
        database="a02",                     # Optional: specify your database
        schema="your_schema"                # Optional: specify your schema
    )