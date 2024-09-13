from tkinter import *

import mysql.connector


def connect_to_database():
    def on_ok():
        # Retrieve the values from the text widgets
        nonlocal host, user, password, database
        host = T_host.get("1.0", "end-1c").strip()
        user = T_user.get("1.0", "end-1c").strip()
        password = T_pass.get("1.0", "end-1c").strip()
        database = T_db.get("1.0", "end-1c").strip()
        window.destroy()  # Close the window

    # Initialize GUI variables
    host, user, password, database = '', '', '', ''

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

    btnOk = Button(window, text="Ok", command=on_ok)
    btnOk.grid(column=0, row=6)
    btnCancel = Button(window, text="Cancel", command=window.destroy)
    btnCancel.grid(column=1, row=6)

    window.mainloop()  # Enter the Tkinter event loop

    # Return the MySQL connection using the retrieved values
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
