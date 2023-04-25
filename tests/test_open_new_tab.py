from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logging_utility import create_logger

logger = create_logger(__name__, "test_open_new_tab.log", "pass" or "fail")

class TestNewTab:

    def test_open_new_tab(self, browser):
        try:
            # Navigate to the Open in New Tab page
            browser.get("http://localhost:7080/windows")

            # Click the link to open a new tab
            link = browser.find_element(By.LINK_TEXT, "Click Here")
            link.click()

            # Switch to the new tab
            WebDriverWait(browser, 10).until(EC.number_of_windows_to_be(2))
            browser.switch_to.window(browser.window_handles[1])

            # Verify the new tab is opened
            assert browser.title == "New Window"
            logger.info("TestNewTab Passed")

        except:
            # Log an error message and re-raise the exception
            logger.error("TestNewTab Failed")
            raise

