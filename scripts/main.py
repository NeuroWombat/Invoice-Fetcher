from invoice_automizing import *
import sys


def main():
    autopay=autopayAutomation()
    email=sys.argv[1]
    password=sys.argv[2]

    autopay.startBrowser()
    if autopay.login(email,password):
        print(f"Received: {email}, {password}")
        autopay.logout()




if __name__ == "__main__":
    main()
