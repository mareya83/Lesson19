
from Driver import Driver
from tools.Data import Data
from Actions import Action


import random
from time import sleep

drivers = ("chrome", "firefox")


class App:
    def __init__(self, driver):
        self.driver = driver

def main():

    tests = Driver(random.choice(drivers))
    driver = App(tests.__dict__["driver"])
    driver = driver.__dict__["driver"]

    driver.get("https://medium.com")

    Action(driver, Data(driver, "class_name", "bx").find_element()).get_ection()

    Action(driver, Data(driver, "class_name", "button-text-2").find_element()).get_ection()

    sleep(10)


if __name__ == "__main__":
    main()
