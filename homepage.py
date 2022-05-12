import time

from pages.basepage import *


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.usermenu_btn = 'a[data-button-name="Profile picture"]'
        self.logout_btn = 'ul.dropdown-menu a.trackButton[data-button-name="Logout"]'

    def get_title(self):
        title = self.driver.title
        print(title)
        return title

    def click_logout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.usermenu_btn).click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, self.logout_btn).click()
