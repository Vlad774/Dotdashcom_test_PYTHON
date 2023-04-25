from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utilities.logging_utility import create_logger

logger = create_logger(__name__, "test_iframe.log", "pass" or "fail")


class TestIframe:

    def test_iframe_text(self, browser):
        try:
            # Navigate to the iframe page
            browser.get("http://localhost:7080/iframe")

            # Switch to the iframe
            iframe = browser.find_element(By.CSS_SELECTOR, "iframe")
            browser.switch_to.frame(iframe)

            # Wait for the element to be visible
            wait = WebDriverWait(browser, 10)
            editor = wait.until(EC.visibility_of_element_located((By.ID, "tinymce")))

            # Find the editable field and type some text
            editor.clear()
            editor.send_keys("Hello")
            time.sleep(2)

            # Switch back to the main frame
            browser.switch_to.default_content()

            # Verify that the typed text is displayed
            assert browser.find_element(By.XPATH, "(//p[normalize-space()='Hello'])[1]").text == "Hello"
            # Log a success message
            logger.info("TestIframe Passed")

        except:
            # Log an error message and re-raise the exception
            logger.error("TestIframe Failed")
            raise

        time.sleep(2)
