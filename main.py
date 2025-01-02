from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import tkinter as tk

driver = webdriver.Firefox()


def login(email, password):
    driver.get('https://app.autopay.eu/login')

    # Accepting cookies to input user data and press login button
    time.sleep(1)
    driver.find_element(By.ID, 'cmpwelcomebtnyes').click()
    time.sleep(1)  # Wait for cookies pop-up to disappear

    email_input = driver.find_element(By.ID, 'email')
    pass_input = driver.find_element(By.ID, 'password')
    submit_BTN = driver.find_element(By.XPATH, "//button[@type='submit']")

    email_input.send_keys(email)
    pass_input.send_keys(password)
    submit_BTN.click()

    # Checking if login was successful by changing url to dashboard
    time.sleep(2)  # Wait for change of site
    if "dashboard" in driver.current_url:
        return True
    else:
        print("Login error")

    return False


def logoutClose():
    driver.get('https://app.autopay.eu/dashboard')

    logout_BTN = driver.find_element(By.CLASS_NAME,'autopay-header__logout')
    logout_BTN.click()

    driver.quit()


def getInvoices():
    driver.get('https://app.autopay.eu/invoices')
    time.sleep(3)  # Wait for site load

    # Setting limit selector to maximum [50]
    invoice_limit = driver.find_element(By.XPATH,'//autopay-select[@name="pageLimit"]//div[@class="ngx-select__toggle btn form-control"]')
    invoice_limit.click()
    limit_option = driver.find_element(By.XPATH,'//span[text()="50"]')
    limit_option.click()

    # Version for time from select
    time_period = driver.find_element(By.XPATH,'//autopay-select[@name="period"]//div[@class="ngx-select__toggle btn form-control"]')
    time_period.click()
    tP_option = driver.find_element(By.XPATH,'//span[text()="The last 30 days"]')
    tP_option.click()

    '''Version for selecting exact data
    start_time=
    end_time=

    '''
    # Apply time period change
    driver.find_element(By.XPATH,'//button[@type="submit"]').click()
    time.sleep(1)

    # Downloading invoices
    #directory="C:\Program Files\Autopay"
    pages = driver.find_elements(By.XPATH,'//div[@class="pagination-pages"]//a')
    last_page = int(pages[-2].text)

    for i in range(0,last_page):
        time.sleep(10)  # Wait to load page
        buttons = driver.find_elements(By.XPATH,'//a[@class="download-link ng-star-inserted"]')     # Gets all of PDFs download buttons
        for j in range(0,len(buttons)):
            buttons[j].click()          #Downloads invoice

        pages[-1].click()     # Pointing to the last element which is next page <a>

def printInvoices():
    return True


def GUI():
    return True


def main():
    l = input("Enter your email: ")
    p = input("Enter your password: ")
    mode = input("Enter mode of filtering invoices [The last 30 days, Current month, Previous month, All history, Any date]: ")
    if mode != "The last 30 days" and mode != "":
        start = input("Select starting date [YYYY-MM-DD]: ")
        end = input("Select ending date [YYYY-MM-DD]: ")
        # Add prefix to choose right date

    print=input("Do you wanna print the invoices? [Y/N]: ")
    if (login(l, p)):
        getInvoices()

        logoutClose()


if __name__ == "__main__":
    main()
