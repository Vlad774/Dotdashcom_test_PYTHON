import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logging_utility import create_logger

logger = create_logger(__name__, "test_dynamic_controls.log", "pass" or "fail")

@pytest.mark.dynamic_controls
class TestDynamicControls:

    def test_remove_add_checkbox_and_toggle_textbox(self, browser):
        try:
            # Navigate to the Dynamic Controls page
            browser.get("http://localhost:7080/dynamic_controls")

            # Wait for the Remove button and click it, then wait for checkbox to be removed
            remove_button = browser.find_element(By.CSS_SELECTOR, "#checkbox-example button").click()
            WebDriverWait(browser, 10).until_not(EC.presence_of_element_located((By.ID, "checkbox")))

            # Assert that checkbox is gone
            assert len(browser.find_elements(By.ID, "checkbox")) == 0

            # Wait for the Add button and click it, then wait for checkbox to be added
            add_button = browser.find_element(By.CSS_SELECTOR, "#checkbox-example button").click()
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "checkbox")))

            # Assert that checkbox is present
            assert len(browser.find_elements(By.ID, "checkbox")) > 0

            # Wait for the Enable button and click it, then wait for text box to be enabled
            enable_button = browser.find_element(By.CSS_SELECTOR, "#input-example button").click()
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example input")))

            # Assert that text box is enabled
            assert browser.find_element(By.CSS_SELECTOR, "#input-example input").is_enabled()

            # Wait for the Disable button and click it, then wait for text box to be disabled
            disable_button = browser.find_element(By.CSS_SELECTOR, "#input-example button").click()
            WebDriverWait(browser, 10).until_not(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example input")))

            # Assert that text box is disabled
            assert not browser.find_element(By.CSS_SELECTOR, "#input-example input").is_enabled()

            logger.info("Dynamic Controls Test Passed")
        except:
            logger.error("Dynamic Controls Test Failed")
            raise
