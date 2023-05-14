from selenium.webdriver.common.by import By

class CreateAccountPage:

    name = (By.XPATH, '//input[@id="ap_customer_name"]')
    phone = (By.XPATH, '//input[@id="ap_phone_number"]')
    email = (By.XPATH, '//input[@type="email"]')
    password = (By.XPATH, '//input[@type="password"]')
    continuebutton = (By.XPATH, '//input[@id="continue"]')
    error = (By.XPATH, '//span[@class="a-list-item"]')

    def __init__(self, driver):
        self.driver = driver

    def checkingpage(self):
        registration_page = self.driver.title
        assert registration_page == "Amazon Registration"
        print("Legit page")

    def entername(self):
        return self.driver.find_element(*CreateAccountPage.name).send_keys("Krishnaditya Rana")

    def phonenumber(self):
        return self.driver.find_element(*CreateAccountPage.phone).send_keys("9033386727")

    def emailid(self):
        return self.driver.find_element(*CreateAccountPage.email).send_keys("abc@gmail.com")

    def enterpassword(self):
        return self.driver.find_element(*CreateAccountPage.password).send_keys("ABC@123$")

    def continuebtn(self):
        return self.driver.find_element(*CreateAccountPage.continuebutton).click()

    def errorprinter(self):
        errortext = self.driver.find_element(*CreateAccountPage.error)
        return print(errortext.text)

