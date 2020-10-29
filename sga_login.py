
from selenium.webdriver.common.keys import Keys


class SgaLogin:

    def __init__(self, user, password, driver):
        self.user = user
        self.password = password
        self.driver = driver

    def login(self):
        self.get_input_user().send_keys(self.user)
        self.get_input_password().send_keys(self.password)
        self.get_input_password().send_keys(Keys.ENTER)

    def get_input_user(self):
        return self.driver.find_element_by_xpath('//*[@title="Nickname"]')

    def get_input_password(self):
        return self.driver.find_element_by_xpath('//*[@title="Contraseña"]')
