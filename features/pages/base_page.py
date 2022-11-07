
class BasePage:

    URL = ""

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        self.get_current_url()

    def go_home(self):
        return self.driver.current_url
