import sqlite3
from tkinter import *

def sql(event=None):
    username = T_username.get(1.0, "end-1c")
    password = T_pass.get(1.0,"end-1c")
    extract_details(username,password)

def extract_details(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    stmt = "SELECT password FROM users WHERE username = ?"
    cursor.execute(stmt, (username,))
    results = cursor.fetchall()
    if(results[0][0]==password):
        print(password)
        #login here!


window = Tk()
window.title("PyQuery v1")
window.geometry('450x100')
window.tk.call('tk', 'scaling', 3.0)
lbl_username = Label(window, text="Username: ")
lbl_username.grid(column=0, row=0)
T_username = Text(window, height=1, width=15)
T_username.grid(column=1, row=0)
lbl_pass = Label(window, text="Password: ")
lbl_pass.grid(column=0, row=1)
T_pass = Text(window, height=1, width=15)
T_pass.grid(column=1, row=1)
btnOk = Button(window, text="Ok", command=sql)
btnOk.grid(column=0, row=3)
window.bind('<Return>', sql)
btnCancel = Button(window, text="Cancel", command=window.destroy)
btnCancel.grid(column=3, row=3)




window.mainloop()