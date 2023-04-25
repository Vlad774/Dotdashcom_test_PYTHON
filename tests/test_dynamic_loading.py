import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logging_utility import create_logger

logger = create_logger(__name__, "test_dynamic_loading.log", "pass" or "fail")

@pytest.mark.dynamic_loading
class TestDynamicLoading:

    def test_dynamic_loading(self, browser):
        try:
            # Navigate to the Dynamic Loading page
            browser.get("http://localhost:7080/dynamic_loading/2")

            # Wait for the Start button to be clickable
            start_button = browser.find_element(By.CSS_SELECTOR, "div[id='start'] button").click()

            # Wait for the text "Hello World!" to be visible
            hello_world_text = WebDriverWait(browser, 60).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='finish'] h4")))

            # Verify that the text "Hello World!" is displayed
            assert hello_world_text.text == "Hello World!"
            # Wait time secondsdown
            time.sleep(3)

            logger.info("Dynamic Loading Test Passed")
        except:
            logger.error("Dynamic Loading Test Failed")
            raise

