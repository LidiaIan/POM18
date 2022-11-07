from selenium.webdriver.common.by import By
from base_page import BasePage


class ThanksPage(BasePage):
    URL = "https://formy-project.herokuapp.com/thanks"

    def get_message_text(self):
        message_element = self.driver.find_element(By.CLASS_NAME, "alert")
        return message_element.text

