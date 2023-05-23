from selenium.webdriver.common.by import By

from time import sleep

class Data:
    def __init__(self, driver, idetifire, value):
        self.driver = driver
        self.idetifire =idetifire 
        self.value = value


    def find_element(self):
        sleep(5)
        if self.idetifire == "id":
            return self.driver.find_element(By.ID, self.value)
        
        if self.idetifire == "class_name":
            return self.driver.find_element(By.CLASS_NAME, self.value)

        if self.idetifire == "xpath":
            return self.driver.find_element(By.XPATH, self.value)

    def find_elements(self):
        sleep(5)
        if self.idetifire == "id":
            return self.driver.find_elements(By.ID, self.value)
        
        if self.idetifire == "class_name":
            return self.driver.find_elements(By.CLASS_NAME, self.value)

        if self.idetifire == "xpath":
            return self.driver.find_elements(By.XPATH, self.value)

