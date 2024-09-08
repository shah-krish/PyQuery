from tkinter import *

def sql():
    pass

window = Tk()
window.title("PyQuery v1")
window.geometry('900x200')
window.tk.call('tk', 'scaling', 2.0)


for i in range(12):
    window.grid_columnconfigure(i, weight=1)

# Configure grid rows
window.grid_rowconfigure(3, weight=1)

btn_mysql = Button(window, text="MySQL", command=sql)
btn_mysql.grid(column=2, row=3, padx=15, pady=10, sticky='ew')

btn_postgres = Button(window, text="Postgres", command=sql)
btn_postgres.grid(column=4, row=3, padx=15, pady=10, sticky='ew')

btn_redshift = Button(window, text="Redshift", command=sql)
btn_redshift.grid(column=6, row=3, padx=15, pady=10, sticky='ew')

btn_snowflake = Button(window, text="Snowflake", command=sql)
btn_snowflake.grid(column=8, row=3, padx=15, pady=10, sticky='ew')

btn_bigquery = Button(window, text="BigQuery", command=sql)
btn_bigquery.grid(column=10, row=3, padx=15, pady=10, sticky='ew')
window.mainloop()
