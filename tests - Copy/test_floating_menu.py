from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utilities.logging_utility import create_logger

logger = create_logger(__name__, "test_floating_menu.log", "pass" or "fail")


class TestFloatingMenu:

    def test_floating_menu(self, browser):
        # Navigate to the Floating Menu page
        browser.get("http://localhost:7080/floating_menu")

        # Scroll down the page
        html = browser.find_element(By.TAG_NAME, "html")
        html.send_keys(Keys.END)

        # Wait for the floating menu to be displayed
        try:
            WebDriverWait(browser, 3).until(
                EC.visibility_of_element_located((By.ID, "page-footer"))
            )

            # Assert that the floating menu is displayed
            assert browser.find_element(By.ID, "page-footer").is_displayed()

            # Log a success message
            logger.info("Floating Menu Test Passed")

        except:
            # Log an error message and re-raise the exception
            logger.error("Floating Menu Test Failed")
            raise

        # Wait time seconds
        time.sleep(2)
