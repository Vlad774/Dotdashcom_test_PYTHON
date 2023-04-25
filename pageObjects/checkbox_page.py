from selenium.webdriver.common.by import By


class CheckboxPage:
    # locators
    checkbox1 = (By.CSS_SELECTOR, "input[type='checkbox']:nth-of-type(1)")
    checkbox2 = (By.CSS_SELECTOR, "input[type='checkbox']:nth-of-type(2)")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get("http://localhost:7080/checkboxes")

    def checkbox1_checked(self):
        return self.browser.find_element(*self.checkbox1).is_selected()

    def checkbox2_checked(self):
        return self.browser.find_element(*self.checkbox2).is_selected()

    def check_checkbox1(self):
        self.browser.find_element(*self.checkbox1).click()

    def uncheck_checkbox2(self):
        self.browser.find_element(*self.checkbox2).click()
