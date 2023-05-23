
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class Action:
    def __init__(self, driver, input):
        self.driver = driver
        self.input = input

    def get_ection(self):
            sleep(3)
            ActionChains(self.driver).click(self.input).perform()
            sleep(10)


