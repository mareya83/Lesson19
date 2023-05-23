from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


driver = None

class Driver:
    def __init__(self, webdriver_type):
        if webdriver_type == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
        if webdriver_type == "firefox":
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

