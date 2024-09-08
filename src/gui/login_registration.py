import sqlite3
from tkinter import *

class LoginManager:
    def __init__(self):
        self.login = False
        self.window = None

    def sql(self, event=None):
        username = self.T_username.get(1.0, "end-1c")
        password = self.T_pass.get(1.0, "end-1c")
        self.extract_details(username, password)

    def extract_details(self, username, password):
        conn = sqlite3.connect("../database_sqlite/users.db")
        cursor = conn.cursor()
        stmt = "SELECT password FROM users WHERE username = ?"
        cursor.execute(stmt, (username,))
        results = cursor.fetchall()
        self.authorize(results, password)

    def setup_gui(self):
        self.window = Tk()
        self.window.title("PyQuery v1")
        self.window.geometry('450x200')
        self.window.tk.call('tk', 'scaling', 2.0)

        lbl_username = Label(self.window, text="Username: ")
        lbl_username.grid(column=0, row=0)

        self.T_username = Text(self.window, height=1, width=15)
        self.T_username.grid(column=1, row=0)
        self.T_username.focus_set()

        lbl_pass = Label(self.window, text="Password: ")
        lbl_pass.grid(column=0, row=1)

        self.T_pass = Text(self.window, height=1, width=15)
        self.T_pass.grid(column=1, row=1)

        btnOk = Button(self.window, text="Ok", command=self.sql)
        btnOk.grid(column=0, row=3)

        self.window.bind('<Return>', self.sql)

        btnCancel = Button(self.window, text="Cancel", command=self.window.destroy)
        btnCancel.grid(column=3, row=3)

        self.lbl_output = Label(self.window, text="")
        self.lbl_output.grid(column=1, row=2)
        self.window.mainloop()

    def authorize(self, results, password):
        if not results:
            self.lbl_output.config(text="Username or Password is incorrect!")
        elif results[0][0] == password:
            self.lbl_output.config(text="Login Successful!")
            self.window.after(1000, self.window.destroy)
            self.login = True
        else:
            self.lbl_output.config(text="Username or Password is incorrect!")
            self.login = False

    def get_login_status(self):
        return self.login

def main():
    login_manager = LoginManager()
    login_manager.setup_gui()
    print("Login status:", login_manager.get_login_status())

if __name__ == "__main__":
    main()
