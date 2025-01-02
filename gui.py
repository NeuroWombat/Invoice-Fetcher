import tkinter as tk
from tkinter import ttk
from invoice_automizing import *


def createGUI():
    root = tk.Tk()
    root.geometry("600x348")
    root.title("Invoice Automation")

    email = tk.StringVar()
    password = tk.StringVar()
    start_date = tk.StringVar()
    end_date = tk.StringVar()
    print_invoices = tk.BooleanVar()

    options = ['The last 30 days', 'Current month', 'Previous month', 'All history', 'Any date']

    tk.Label(root, text="Invoice Download System", font=("Arial", 16)).grid(column=1, row=0, columnspan=4, pady=10)

    tk.Label(root, text="E-mail:").grid(column=1, row=1, padx=5, sticky="e")
    tk.Entry(root, textvariable=email, width=25).grid(column=2, row=1, padx=5)

    tk.Label(root, text="Password:").grid(column=3, row=1, padx=5, sticky="e")
    tk.Entry(root, textvariable=password, show="*", width=25).grid(column=4, row=1, padx=5)

    tk.Label(root, text="Date Period:").grid(column=1, row=2, padx=5, sticky="e")
    combobox = ttk.Combobox(root, values=options, state='readonly', width=20)
    combobox.set("Select time period")
    combobox.grid(column=2, row=2, columnspan=2, pady=5)

    start_label = tk.Label(root, text="Start Date:")
    start_entry = tk.Entry(root, textvariable=start_date, width=15)
    end_label = tk.Label(root, text="End Date:")
    end_entry = tk.Entry(root, textvariable=end_date, width=15)

    tk.Checkbutton(root, text="Do you want to print invoices?", variable=print_invoices).grid(column=1, row=4, columnspan=4, pady=10)
    tk.Button(root, text="Download Invoices", command=lambda: dataValidation(email.get(), password.get(),[combobox.get(),start_entry.get(),end_entry.get()])).grid(column=1, row=5, columnspan=4, pady=20)

    def on_select(event):
        if combobox.get() == 'Any date':
            start_label.grid(column=1, row=3, padx=5, sticky="e")
            start_entry.grid(column=2, row=3, padx=5)

            end_label.grid(column=3, row=3, padx=5, sticky="e")
            end_entry.grid(column=4, row=3, padx=5)
        else:
            start_label.grid_forget()
            start_entry.grid_forget()
            end_label.grid_forget()
            end_entry.grid_forget()


    combobox.bind("<<ComboboxSelected>>", on_select)


    root.mainloop()


def dataValidation(email, password, mode):
    if email!="" and password!="":
        return True

    return False

