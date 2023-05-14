from selenium.webdriver.common.by import By


class SignInPage:

    clickoncreateaccount = (By.XPATH, '//a[@id="createAccountSubmit"]')

    def __init__(self, driver):
        self.driver = driver

    def redirectosign_In(self):
        signin_windowtab = self.driver.title
        assert signin_windowtab == 'Amazon Sign In'
        print("Redirected to sign-in page ")

    def createyouramazon_Account(self):
        return self.driver.find_element(*SignInPage.clickoncreateaccount).click()
