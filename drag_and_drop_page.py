from selenium.webdriver.common.by import By


class DragAndDropPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "http://localhost:7080/drag_and_drop"

    def open(self):
        self.browser.get(self.url)

    @property
    def source_element(self):
        return self.browser.find_element(By.ID, "column-a")

    @property
    def target_element(self):
        return self.browser.find_element(By.ID, "column-b")
