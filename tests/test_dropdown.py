import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utilities.logging_utility import create_logger

logger = create_logger(__name__, "test_dropdown.log", "pass" or "fail")

@pytest.mark.dropdown
class TestDropdown:

    def test_select_option(self, browser):
        try:
            # Navigate to the dropdown page
            browser.get("http://localhost:7080/dropdown")

            # Find the dropdown element
            dropdown = Select(browser.find_element(By.ID, "dropdown"))

            # Verify that the default option is "Please select an option"
            assert dropdown.first_selected_option.text == "Please select an option"

            # Select Option 1
            dropdown.select_by_visible_text("Option 1")

            # Verify that Option 1 is selected
            assert dropdown.first_selected_option.text == "Option 1"

            # Wait for 3 seconds
            time.sleep(3)

            # Select Option 2
            dropdown.select_by_visible_text("Option 2")

            # Verify that Option 2 is selected
            assert dropdown.first_selected_option.text == "Option 2"

            logger.info("Dropdown Test Passed")
        except:
            logger.error("Dropdown Test Failed")
            raise

