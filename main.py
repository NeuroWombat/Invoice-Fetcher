from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Firefox()


def login(email,password):
    driver.get('https://app.autopay.eu/login')

    # Accepting cookies to input user data and press login button
    driver.find_element(By.ID,'cmpwelcomebtnyes').click()
    time.sleep(1) # Wait for cookies pop-up to disappear

    email_input=driver.find_element(By.ID,'email')
    pass_input=driver.find_element(By.ID,'password')
    submit_BTN=driver.find_element(By.XPATH,"//button[@type='submit']")

    email_input.send_keys(email)
    pass_input.send_keys(password)
    submit_BTN.click()

    # Checking if login was successful by changing url to dashboard
    time.sleep(2) # Wait for change of site
    if "dashboard" in driver.current_url:
        return True
    else:
        print("Błąd logowania")

    return False


def logoutClose():
    driver.get('https://app.autopay.eu/dashboard')

    logout_BTN=driver.find_element(By.CLASS_NAME,'autopay-header__logout')
    logout_BTN.click()

    driver.quit()


def getInvoices(mode):
    driver.get('https://app.autopay.eu/invoices')

    period_mode=driver.find_element(By.CLASS_NAME,'')
    change_period_BTN=driver.find_element(By.CLASS_NAME,'')
    select_number=driver.find_element(By.CLASS_NAME,'')
    pages_number=driver.find_element(By.CLASS_NAME,'')

    #Select(period_mode).select_by_value('Current month')
    #Select(pages_number).select_by_value('50')



def printInvoices():

    return True

def main():
    l=input("Enter your email: ")
    p=input("Enter your password: ")

    if(login(l,p)):
        #mode=input("Enter mode: ")
        printing=input("Do you want to print these invoices? (Y/N): ")

        getInvoices(mode)

        if printing=='Y':
            printInvoices()

        #logoutClose()


if __name__=="__main__":
    main()