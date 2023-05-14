from selenium.webdriver.common.by import By


class Homepage:

    clickonsignin = (By.XPATH, '//span[@id="nav-link-accountList-nav-line-1"]')

    def __init__(self, driver):
        self.driver = driver

    def clickonsign_In(self):
        return self.driver.find_element(*Homepage.clickonsignin).click()

