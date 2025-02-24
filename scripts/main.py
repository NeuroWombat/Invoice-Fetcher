from gui import *
from invoice_automizing import *


def main():
    autopay=autopayAutomation()

    if app.validFlag:
        email_input=app.email.get()
        pass_input=app.password.get()
        mode_input=app.option
        if mode_input=="Any date":
            start_input=start_entry.get()
            end_input=end_entry.get()
        else:
            start_input=None
            end_input=None

        autopay.startBrowser()
        if autopay.login(email_input,pass_input):
            autopay.filterInvoices(mode_input,[start_input,end_input])
            autopay.downloadInvoices()
            if app.printFlag.get():
                autopay.printInvoices()

        autopay.logout()




if __name__ == "__main__":
    main()
