
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
    
    sleep(3)

    nav_panel = Data(driver, "class_name", "n.p").find_element()
    print(nav_panel)

    Action(driver, Data(driver, "class_name", "bs.q").find_element()).get_ection()
    sleep(5)
  
    Action(driver, Data(driver, "class_name", "al.db").find_elements()[4]).get_ection()

    sleep(10)


if __name__ == "__main__":
    main()
