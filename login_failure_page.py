from selenium.webdriver.common.by import By

class LoginFailurePage:
    def __init__(self, browser):
        self.browser = browser
        self.failure_message = browser.find_element(By.CSS_SELECTOR, ".flash.error")
        self.username_field = browser.find_element(By.ID, "username")
        self.password_field = browser.find_element(By.ID, "password")
        self.submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

    def get_failure_message(self):
        return self.failure_message.text
