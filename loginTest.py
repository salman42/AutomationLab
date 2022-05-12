from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pages.loginpage import LoginPage
from pages.homepage import HomePage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = Service('/Users/mac/PycharmProjects/Edurekaa/drivers/chromedriver')
        cls.driver = webdriver.Chrome(service=cls.service)

    def test_login_valid(self):
        driver = self.driver
        self.driver.get('https://www.edureka.co/')
        login = LoginPage(driver)
        login.click_login_window()
        login.enter_useremail("sulmanmansha@gmail.com")
        login.enter_userpassword("Salman123456")
        login.click_login_btn()

        homepage = HomePage(driver)
        time.sleep(2)
        assert "Instructor-Led Online Training with 24X7 Lifetime Support | Edureka" in homepage.get_title()
        time.sleep(2)
        homepage.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")




