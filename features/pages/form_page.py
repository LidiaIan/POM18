from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from base_page import BasePage


class FormPage(BasePage):

    URL = "https://formy-project.herokuapp.com/form"
    PAGE_TITLE = "Complete Web Form"

    def input_first_name(self, first_name):
        first_name_element = self.driver.find_element(By.ID, "first-name")
        first_name_element.send_keys(first_name)

    def input_last_name(self, last_name):
        last_name_element = self.driver.find_element(By.ID, "last-name")
        last_name_element.send_keys(last_name)

    def input_job(self, job):
        job_element = self.driver.find_element(By.ID, "job-title")
        job_element.send_keys(job)

    def input_education(self, education):
        education_element = self.driver.find_element(By.ID, "radio-button-3")
        education_element.send_keys(education)

    def input_gender(self, gender):
        gender_element = self.driver.find_element(By.ID, "checkbox-2")
        gender_element.send_keys(gender)

    def input_years(self, years):
        years_element = self.driver.find_element(By.ID, "select - menu")
        years_element.send_keys(years)

    def input_date(self, job):
        date_element = self.driver.find_element(By.ID, "datepicker")
        date_element.send_keys(job)

    def click_submit(self):
        submit_button = self.driver.find_element(By.CLASS_NAME, "btn-primary")
        submit_button.click()

    def clean_first_name(self):
        first_name_element = self.driver.find_element(By.ID, "first-name")
        first_name_element.send_keys(Keys.CONTROL + "a")
        first_name_element.send_keys(Keys.BACKSPACE)