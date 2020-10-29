from selenium.webdriver.common.keys import Keys


class SgaLink:

    def __init__(self, name, driver):
        self.name = name
        self.driver = driver

    def execute_link_element(self):
        self.get_link_element().send_keys(Keys.ENTER)

    def get_link_element(self):
        return self.driver.find_element_by_link_text(self.name)
