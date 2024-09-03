import mysql.connector
from tkinter import *


def sql():
    try:
        query = T.get(1.0, "end-1c").strip()

        # Check if the query is empty
        if not query:
            lbl2.config(text="No query provided.")
            return

        # Execute the SQL query (NEW FUNCTION - Connection)
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        # Display the results in the label (NEW FUNCTION - Display)
        if results:
            result_text = "\n".join(str(row) for row in results)
            lbl2.config(text=result_text)
        else:
            lbl2.config(text="No results found.")
    except Exception as e:
            lbl2.config(text="SQL Query syntax not correct")
    #finally:
    #        conn.close()

#New function - ConnectionValues
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="krish123",
    database="a02"
)

window = Tk()
window.title("PyQuery v1")
window.geometry('900x150')
window.tk.call('tk', 'scaling', 3.0)
lbl = Label(window, text="Enter SQL Query: ")
lbl.grid(column=0, row=0)
lbl2 = Label(window, text="")
lbl2.grid(column=1, row=2)
T = Text(window, height=1, width=30)
T.grid(column=1, row=0)
btnOk = Button(window, text="Ok", command=sql)
btnOk.grid(column=0, row=3)

btnCancel = Button(window, text="Cancel",command=window.destroy)
btnCancel.grid(column=3, row=3)

window.mainloop()

conn.close()

