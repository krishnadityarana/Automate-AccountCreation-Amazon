from selenium.webdriver.common.by import By

class MakingChanges:

    clearingemailfield = (By.XPATH, '//input[@type="email"]')
    n_email = (By.XPATH, '//input[@type="email"]')
    n_pass = (By.XPATH, '//input[@type="password"]')
    n_continueclick = (By.XPATH, '//input[@id="continue"]')

    def __init__(self, driver):
        self.driver = driver

    def clearemailfield(self):
        return self.driver.find_element(*MakingChanges.clearingemailfield).clear()

    def newemail(self):
        return self.driver.find_element(*MakingChanges.n_email).send_keys("efg@gmail.com")

    def newpassword(self):
        return self.driver.find_element(*MakingChanges.n_pass).send_keys("ABC@123$")

    def reclickcontinuebtn(self):
        return self.driver.find_element(*MakingChanges.n_continueclick).click()


