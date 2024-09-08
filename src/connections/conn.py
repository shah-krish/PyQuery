import mysql.connector
import psycopg2
import snowflake.connector
from google.cloud import bigquery


class ConnectionManager:
    def __init__(self, mysql_config=None, postgres_config=None, redshift_config=None, snowflake_config=None,
                 bigquery_config=None):
        # MySQL configuration
        if mysql_config:
            self.mysql_host = mysql_config.get('host', 'localhost')
            self.mysql_user = mysql_config.get('user')
            self.mysql_password = mysql_config.get('password')
            self.mysql_database = mysql_config.get('database')

        # PostgreSQL configuration
        if postgres_config:
            self.postgres_host = postgres_config.get('host', 'localhost')
            self.postgres_user = postgres_config.get('user')
            self.postgres_password = postgres_config.get('password')
            self.postgres_database = postgres_config.get('database')

        # Redshift configuration
        if redshift_config:
            self.redshift_host = redshift_config.get('host')
            self.redshift_port = redshift_config.get('port', '5439')
            self.redshift_user = redshift_config.get('user')
            self.redshift_password = redshift_config.get('password')
            self.redshift_database = redshift_config.get('database')

        # Snowflake configuration
        if snowflake_config:
            self.snowflake_user = snowflake_config.get('user')
            self.snowflake_password = snowflake_config.get('password')
            self.snowflake_account = snowflake_config.get('account')
            self.snowflake_warehouse = snowflake_config.get('warehouse')
            self.snowflake_database = snowflake_config.get('database')
            self.snowflake_schema = snowflake_config.get('schema')

        # BigQuery configuration
        if bigquery_config:
            self.bigquery_credentials = bigquery_config.get(
                'credentials')  # Assume credentials are provided for BigQuery

    def connect_to_mysql(self):
        # if not all([self.mysql_user, self.mysql_password, self.mysql_database]):
        #     raise ValueError("MySQL connection parameters are missing")
        return mysql.connector.connect(
            host=self.mysql_host,
            user=self.mysql_user,
            password=self.mysql_password,
            database=self.mysql_database
        )

    def connect_to_postgres(self):
        # if not all([self.postgres_host, self.postgres_user, self.postgres_password, self.postgres_database]):
        #     raise ValueError("PostgreSQL connection parameters are missing")
        return psycopg2.connect(
            host=self.postgres_host,
            user=self.postgres_user,
            password=self.postgres_password,
            database=self.postgres_database
        )

    def connect_to_redshift(self):
        # if not all([self.redshift_host, self.redshift_user, self.redshift_password, self.redshift_database]):
        #     raise ValueError("Redshift connection parameters are missing")
        return psycopg2.connect(
            host=self.redshift_host,
            port=self.redshift_port,
            user=self.redshift_user,
            password=self.redshift_password,
            database=self.redshift_database
        )

    def connect_to_snowflake(self):
        # if not all([self.snowflake_user, self.snowflake_password, self.snowflake_account]):
        #     raise ValueError("Snowflake connection parameters are missing")
        return snowflake.connector.connect(
            user=self.snowflake_user,
            password=self.snowflake_password,
            account=self.snowflake_account,
            warehouse=self.snowflake_warehouse,
            database=self.snowflake_database,
            schema=self.snowflake_schema
        )

    def connect_to_bigquery(self):
        # BigQuery Client initialization assumes credentials are set up correctly in the environment or provided
        return bigquery.Client(credentials=self.bigquery_credentials)
