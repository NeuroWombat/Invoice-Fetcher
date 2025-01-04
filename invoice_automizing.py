from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


class autopayAutomation:
    def __init__(self):
        self.driver = None

    def startBrowser(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://app.autopay.eu/login')

    def login(self,email,password):
        self.driver.find_element(By.ID,'cmpwelcomebtnyes').click()  # Accepting cookies to input user data and press login button
        time.sleep(1)  # Wait for cookies pop-up to disappear

        # Find inputs on website
        email_input = self.driver.find_element(By.ID,'email')
        pass_input = self.driver.find_element(By.ID,'password')
        submit_BTN = self.driver.find_element(By.XPATH,'//button[@type="submit"]')

        email_input.send_keys(email)
        pass_input.send_keys(password)
        submit_BTN.click()

        time.sleep(2)  # Wait for change of site
        if "dashboard" in self.driver.current_url:
            return True
        else:
            print("Login error")

        return False

    def logout(self):
        self.driver.get('https://app.autopay.eu/dashboard')

        time.sleep(1)

        self.driver.find_element(By.CLASS_NAME,'autopay-header__logout').click()
        self.driver.quit()

    def filterInvoices(self,mode,period):
        self.driver.get('https://app.autopay.eu/invoices')
        time.sleep(2)  # Wait for site load

        # Setting limit selector to maximum [50]
        limit_selector = self.driver.find_element(By.XPATH,'//autopay-select[@name="pageLimit"]//div[@class="ngx-select__toggle btn form-control"]')
        limit_selector.click()
        self.driver.find_element(By.XPATH,'//span[text()="50"]').click()

        # Selecting time period
        time_period = self.driver.find_element(By.XPATH,'//autopay-select[@name="period"]//div[@class="ngx-select__toggle btn form-control"]')
        time_period.click()
        period_option = self.driver.find_element(By.XPATH,f'//span[text()="{mode}"]')
        period_option.click()
        if mode == "Any Date":
            start = period[0]
            end = period[1]

        self.driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        time.sleep(1)

    def downloadInvoices(self):
        # directory="C:\Program Files\Autopay"
        pages = self.driver.find_elements(By.XPATH, '//div[@class="pagination-pages"]//a')
        last_page = int(pages[-2].text)

        for i in range(0,last_page):
            time.sleep(2)  # Wait to load page
            buttons = self.driver.find_elements(By.XPATH,'//a[@class="download-link ng-star-inserted"]')  # Gets all of PDFs download buttons
            for j in range(0,len(buttons)):
                buttons[j].click()  # Downloads invoice

            pages[-1].click()  # Pointing to the last element which is next page <a>


    def printInvoices(self):
        return True
