import psycopg2
def connect_to_database():
    return psycopg2.connect(
        host="your-redshift-cluster-endpoint",
        # Redshift cluster endpoint (e.g., "mycluster.abc123xyz.us-west-2.redshift.amazonaws.com")
        port="5439",  # Default port for Redshift
        user="your_username",  # Your Redshift username
        password="your_password",  # Your Redshift password
        database="your_database"  # Your Redshift database name
    )