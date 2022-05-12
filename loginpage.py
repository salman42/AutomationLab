from pages.basepage import *


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.user_email_textbox_id = "si_popup_email"
        self.user_password_textbox_id = "si_popup_passwd"
        self.login_form_btn = 'span[ data-button-name="Login"]'
        self.login_btn = 'button[class="clik_btn_log btn-block"]'

    def click_login_window(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_form_btn).click()
        time.sleep(2)

    def enter_useremail(self, useremail):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.ID, self.user_email_textbox_id))
        time.sleep(2)
        action.click()
        self.driver.find_element(By.ID, self.user_email_textbox_id).send_keys(useremail)
        time.sleep(2)
        action.perform()

    def enter_userpassword(self, userpassword):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.ID, self.user_password_textbox_id))
        time.sleep(2)
        action.click()
        self.driver.find_element(By.ID, self.user_password_textbox_id).send_keys(userpassword)
        time.sleep(2)
        action.perform()

    def click_login_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_btn).click()
