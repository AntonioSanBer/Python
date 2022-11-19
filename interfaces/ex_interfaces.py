import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

# username
username_label = ttk.Label(window, text='Username:')
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=10, pady=10)
username_entry = ttk.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.W, padx=10, pady=10)

# password
username_label = ttk.Label(window, text="Password:")
username_label.grid(column=0, row=1, sticky=tkinter.W, padx=10, pady=10)
username_password = ttk.Entry(window, show='*')
username_password.grid(column=1, row=1, sticky=tkinter.W, padx=10, pady=10)

# login button
login_button = ttk.Button(window, text='login')
login_button.grid(column=1, row=3, sticky=tkinter.E, padx=10, pady=10)

window.mainloop()
