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


def getInvoices():
    driver.get('https://app.autopay.eu/invoices')
    time.sleep(2) # Wait for site load

    # Setting limit selector to maximum [50]
    invoice_limit=driver.find_element(By.XPATH,'//autopay-select[@name="pageLimit"]//div[@class="ngx-select__toggle btn form-control"]')
    invoice_limit.click()
    limit_option=driver.find_element(By.XPATH,'//span[text()="50"]')
    limit_option.click()



    # Version for time from select
    time_period=driver.find_element(By.XPATH,'//autopay-select[@name="period"]//div[@class="ngx-select__toggle btn form-control"]')
    time_period.click()
    tP_option=driver.find_element(By.XPATH,'//span[text()="The last 30 days"]')
    tP_option.click()

    '''Version for selecting exact data
    start_time=
    end_time=
    
    '''
    # Apply time period change
    driver.find_element(By.XPATH,'//button[@type="submit"]').click()
    time.sleep(1)

    #Downloading invoices
    directory=""
    pages_BTNs=driver.find_elements(By.XPATH,'//div[@class="pagination-pages"]//a')
    pages=int(len(pages_BTNs)/2 -2)    # Divide by 2 because there's 2 divs with page numbers, also -2 for arrows

    for i in range(pages):
        pages_BTNs[i].click()
        #get all table of invoices




def printInvoices():

    return True

def main():
    l=input("Enter your email: ")
    p=input("Enter your password: ")

    if(login(l,p)):
        #mode=input("Enter mode: ")
        #printing=input("Do you want to print these invoices? (Y/N): ")
        getInvoices()

        #if printing=='Y':
        #    printInvoices()

        #logoutClose()


if __name__=="__main__":
    main()