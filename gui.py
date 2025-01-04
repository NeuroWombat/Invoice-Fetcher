import tkinter as tk
from tkinter import ttk
from invoice_automizing import *

class appInterface:
    def __init__(self):
        self.validFlag=False
        self.printFlag = None
        self.email = None
        self.password = None
        self.option = None
        self.start_date = None
        self.end_date = None

        self.createGUI()

    def createGUI(self):
        root=tk.Tk()
        root.geometry("600x348")
        root.title("Invoice Automation")
        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.start_date = tk.StringVar()
        self.end_date = tk.StringVar()
        self.printFlag = tk.BooleanVar()
        options = ['The last 30 days', 'Current month', 'Previous month', 'All history', 'Any date']


        tk.Label(root, text="E-mail:").grid(column=1, row=1, padx=5, sticky="e")
        tk.Entry(root, textvariable=self.email, width=25).grid(column=2, row=1, padx=5)
        tk.Label(root, text="Password:").grid(column=3, row=1, padx=5, sticky="e")
        tk.Entry(root, textvariable=self.password, show="*", width=25).grid(column=4, row=1, padx=5)
        tk.Label(root, text="Date Period:").grid(column=1, row=2, padx=5, sticky="e")
        combobox = ttk.Combobox(root, values=options, state='readonly', width=20)
        combobox.set("Select time period")
        combobox.grid(column=2, row=2, columnspan=2, pady=5)
        start_label = tk.Label(root, text="Start Date:")
        start_entry = tk.Entry(root, textvariable=self.start_date, width=15)
        end_label = tk.Label(root, text="End Date:")
        end_entry = tk.Entry(root, textvariable=self.end_date, width=15)
        tk.Checkbutton(root, text="Do you want to print invoices?", variable=self.printFlag).grid(column=1, row=4, columnspan=4, pady=10)
        tk.Button(root, text="Download Invoices", command=lambda: self.dataValidation(root,combobox)).grid(column=1, row=5, columnspan=4, pady=20)

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

    def dataValidation(self,root,combobox):
        email=self.email.get()
        password=self.password.get()
        start_date=self.start_date.get()
        end_date=self.end_date.get()

        if email!="" and password!="":
            self.validFlag=True
            self.option=combobox.get()
            root.quit()

        return False
