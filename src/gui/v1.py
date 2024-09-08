from src.connections import mysql_connector
from tkinter import *
from src.gui import login_registration as login

conn = None
lbl2 = None
T = None


def execute_sql_query(query):
    global conn
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def sql(event=None):
    query = T.get(1.0, "end-1c")

    if not query:
        lbl2.config(text="No query provided.")
        return

    try:
        results = execute_sql_query(query)
        display_query_result(results)
    except Exception as e:
        lbl2.config(text="SQL Query syntax not correct")

def display_query_result(results):

    if results:
        result_text = "\n".join(str(row) for row in results)
        lbl2.config(text=result_text)
    else:
        lbl2.config(text="No results found.")

def setup_gui():
    global lbl2, T

    window = Tk()
    window.title("PyQuery v1")
    window.geometry('900x200')
    window.tk.call('tk', 'scaling', 3.0)

    lbl = Label(window, text="Enter SQL Query: ")
    lbl.grid(column=0, row=0)
    lbl2 = Label(window, text="")
    lbl2.grid(column=1, row=2)

    T = Text(window, height=1, width=30)
    T.grid(column=1, row=0)

    btnOk = Button(window, text="Ok", command=sql)
    btnOk.grid(column=0, row=3)

    window.bind('<Return>', sql)

    btnCancel = Button(window, text="Cancel", command=window.destroy)
    btnCancel.grid(column=3, row=3)

    window.mainloop()

def close_connection():
    global conn
    if conn:
        conn.close()

def main():
    global conn

    login_manager = login.LoginManager()
    login_manager.setup_gui()


    if login_manager.get_login_status():
        conn = mysql_connector.connect_to_database()
        try:
            setup_gui()
        finally:
            close_connection()
    else:
        print("Login failed, closing application.")
        close_connection()

if __name__ == "__main__":
    main()
