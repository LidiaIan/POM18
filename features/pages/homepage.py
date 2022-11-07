import time
from selenium.webdriver.common.by import By
from base_page import BasePage


class Homepage(BasePage):

    URL = "https://formy-project.herokuapp.com/"

    def go_to(self, url_text):
        element = self.driver.find_element(By.LINK_TEXT, url_text)
        element.click()

    def click_components_menu(self):
        ac = ActionChains(self.driver)
        components_submenu = self.driver.find_element(By.ID, "navbarDropdownMenuLink")
        ac.move_to_element(components_submenu).click().perform()
        time.sleep(3)