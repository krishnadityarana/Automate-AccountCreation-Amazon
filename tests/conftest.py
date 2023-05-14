import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture(scope="class")
def browser_Invocation(request):
    chrome_opt = Options()
    chrome_opt.add_experimental_option('detach', True)
    service_obj = Service(r"C:\Users\STELLA\Downloads\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj, options=chrome_opt)
    ac = ActionChains(driver)
    # Code
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    print(driver.current_url)
    print(driver.title)
    request.cls.driver= driver
    yield
    driver.close()
