from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logging_utility import create_logger

logger = create_logger(__name__, "test_javascript_error.log", "pass" or "fail")

class TestJsError:

    def test_find_js_error(self, browser):
        try:
            # Navigate to the JavaScript Error page
            browser.get("http://localhost:7080/javascript_error")

            # Wait for the page to finish loading
            wait = WebDriverWait(browser, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, "//body[contains(text(),'Cannot read property')]")))

            # Get the error message
            error_message = browser.find_element(By.XPATH, "//body[contains(text(),'Cannot read property')]").text

            # Log a success message
            logger.info("TestJsError Passed")

        except:
            # Log an error message and re-raise the exception
            logger.error("TestJsError Failed")
            raise
