from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class ContextMenuPage:
    def __init__(self, browser):
        self.browser = browser
        self.box = (By.ID, "hot-spot")

    def right_click_box(self):
        ActionChains(self.browser).context_click(self.browser.find_element(*self.box)).perform()
