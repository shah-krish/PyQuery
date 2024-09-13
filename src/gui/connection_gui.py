from tkinter import *
from tkinter import font
import src.connections as conn_module  # Import your connection module

class DatabaseConnector:
    def __init__(self, mysql_config=None, postgres_config=None, redshift_config=None, snowflake_config=None, bigquery_config=None):
        # Initialize connection configurations
        self.mysql_config = mysql_config
        self.postgres_config = postgres_config
        self.redshift_config = redshift_config
        self.snowflake_config = snowflake_config
        self.bigquery_config = bigquery_config

    def mysql_gui(self):
        window = Tk()
        window.title("PyQuery v1")
        window.geometry('900x200')
        window.tk.call('tk', 'scaling', 2.0)

        lbl_host = Label(window, text="Enter host: ")
        lbl_user = Label(window, text="Enter user: ")
        lbl_pass = Label(window, text="Enter password: ")
        lbl_db = Label(window, text="Enter database: ")
        lbl_host.grid(column=0, row=0)
        lbl_user.grid(column=0, row=1)
        lbl_pass.grid(column=0, row=2)
        lbl_db.grid(column=0, row=3)
        T_host = Text(window, height=1, width=30)
        T_host.grid(column=1, row=0)
        T_user = Text(window, height=1, width=30)
        T_user.grid(column=1, row=1)
        T_pass = Text(window, height=1, width=30)
        T_pass.grid(column=1, row=2)
        T_db = Text(window, height=1, width=30)
        T_db.grid(column=1, row=3)
        btnOk = Button(window, text="Ok")
        btnOk.grid(column=0, row=6)
        btnCancel = Button(window, text="Cancel", command=window.destroy)
        btnCancel.grid(column=3, row=6)

        conn_values = []

        conn_values[0] = T_host.get("1.0", "end-1c").strip()
        conn_values[1] = T_user.get("1.0", "end-1c").strip()
        conn_values[2] = T_pass.get("1.0", "end-1c").strip()
        conn_values[3] = T_db.get("1.0", "end-1c").strip()
        window.mainloop()
        return conn_values

    def connect_to_mysql(self):
        # Placeholder method to connect to MySQL
        conn_values = self.mysql_gui

        self.mysql_config['database'] = conn_values[0]
        self.mysql_config['database'] = conn_values[1]
        self.mysql_config['database'] = conn_values[2]
        self.mysql_config['database'] = conn_values[3]

    def connect_to_postgres(self):
        # Placeholder method to connect to PostgreSQL
        print("Connecting to PostgreSQL...")
        # Implement your connection logic here

    def connect_to_redshift(self):
        # Placeholder method to connect to Redshift
        print("Connecting to Redshift...")
        # Implement your connection logic here

    def connect_to_snowflake(self):
        # Placeholder method to connect to Snowflake
        print("Connecting to Snowflake...")
        # Implement your connection logic here

    def connect_to_bigquery(self):
        # Placeholder method to connect to BigQuery
        print("Connecting to BigQuery...")
        # Implement your connection logic here

# Define your configurations
mysql_config = {

}

postgres_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'krish123',
    'database': 'a02'
}

redshift_config = {
    'host': 'your-redshift-cluster-endpoint',
    'port': '5439',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database'
}

snowflake_config = {
    'user': 'your_user',
    'password': 'your_password',
    'account': 'your_account_identifier',
    'warehouse': 'your_warehouse',
    'database': 'your_database',
    'schema': 'your_schema'
}

bigquery_config = {
    'credentials': None  # Replace with your BigQuery credentials if needed
}


db_connector = DatabaseConnector(
    mysql_config=mysql_config,
    postgres_config=postgres_config,
    redshift_config=redshift_config,
    snowflake_config=snowflake_config,
    bigquery_config=bigquery_config
)

def connect_mysql():
    db_connector.connect_to_mysql()

def connect_postgres():
    db_connector.connect_to_postgres()

def connect_redshift():
    db_connector.connect_to_redshift()

def connect_snowflake():
    db_connector.connect_to_snowflake()

def connect_bigquery():
    db_connector.connect_to_bigquery()

# Create the Tkinter window
# window = Tk()
# window.title("PyQuery v1")
# window.geometry('900x200')
# window.tk.call('tk', 'scaling', 2.0)
#
# lbl_prompt = Label(window, text="Select Database:", font=font.Font(size=14))
# lbl_prompt.grid(column=2, row=0)
#
# # Configure grid columns
# for i in range(12):
#     window.grid_columnconfigure(i, weight=1)
#
# # Configure grid rows
# window.grid_rowconfigure(3, weight=1)
#
# # Create buttons with appropriate commands
# btn_mysql = Button(window, text="MySQL", command=connect_mysql)
# btn_mysql.grid(column=2, row=3, padx=15, pady=10, sticky='ew')
#
# btn_postgres = Button(window, text="Postgres", command=connect_postgres)
# btn_postgres.grid(column=4, row=3, padx=15, pady=10, sticky='ew')
#
# btn_redshift = Button(window, text="Redshift", command=connect_redshift)
# btn_redshift.grid(column=6, row=3, padx=15, pady=10, sticky='ew')
#
# btn_snowflake = Button(window, text="Snowflake", command=connect_snowflake)
# btn_snowflake.grid(column=8, row=3, padx=15, pady=10, sticky='ew')
#
# btn_bigquery = Button(window, text="BigQuery", command=connect_bigquery)
# btn_bigquery.grid(column=10, row=3, padx=15, pady=10, sticky='ew')
#
# # Run the Tkinter event loop
# window.mainloop()
