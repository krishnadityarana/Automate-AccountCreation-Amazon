from selenium.webdriver.common.by import By
from Pageobject.CreateAccountPage import CreateAccountPage
from Pageobject.Homepage import Homepage
from Pageobject.MakingChanges import MakingChanges
from Pageobject.SignInPage import SignInPage
from utilities.BaseClass import BaseClass


class Testclassone(BaseClass):
    def test_registration(self):
     #Clicking on sign in
     homepage = Homepage(self.driver)
     homepage.clickonsign_In()

     # checking if the page redirected or not
     signinpage = SignInPage(self.driver)
     signinpage.redirectosign_In()

     # Clicking on Create amazon account
     signinpage.createyouramazon_Account()

     # Checking the redirected sign up page
     registration_page = self.driver.title
     assert registration_page == "Amazon Registration"

     # Creating a random account that will cause a error
     createaccountpage = CreateAccountPage(self.driver)
     createaccountpage.checkingpage()
     createaccountpage.entername()
     createaccountpage.phonenumber()
     createaccountpage.emailid()
     createaccountpage.enterpassword()
     createaccountpage.continuebtn()
     createaccountpage.errorprinter()


     # making changes accoding to the error meassage
     #The print statements are nothing but, implemented to check if code break's before or after "print()'
     #I have used false data in the whole code , as it is a practice you can use legit data if you want.
     makingchanges = MakingChanges(self.driver)
     makingchanges.clearemailfield()
     print("Field cleared")
     makingchanges.newemail()
     makingchanges.newpassword()
     makingchanges.reclickcontinuebtn()
     print("Details entered congrats")


