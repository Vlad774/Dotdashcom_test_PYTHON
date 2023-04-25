import pytest
from selenium.webdriver.common.by import By
import time
from utilities.logging_utility import create_logger

logger = create_logger(__name__, "test_dynamic_content.log", "pass" or "fail")

@pytest.mark.dynamic_content
class TestDynamicContent:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        try:
            # Navigate to the dynamic content page
            browser.get("http://localhost:7080/dynamic_content")
            # Find the content elements
            self.content_elements = browser.find_elements(By.XPATH,
                                                          "//body/div[@class='row']/div[@id='content']/div[@class='example']/div[@class='row']/div[@id='content']/div[1]")
            logger.info("Dynamic Content Setup Successful")
        except:
            logger.error("Dynamic Content Setup Failed")
            raise

    def test_content_changes_with_page_reload(self, browser):
        try:
            # Get the initial content text
            initial_content_text = [element.text for element in self.content_elements]

            # Get the initial content length
            initial_content_length = len(self.content_elements)

            # Wait for 2 seconds
            time.sleep(2)

            # Reload the page
            browser.refresh()

            # Wait for 2 seconds
            time.sleep(2)

            # Find the content elements again
            new_content_elements = browser.find_elements(By.XPATH,
                                                         "//body/div[@class='row']/div[@id='content']/div[@class='example']/div[@class='row']/div[@id='content']/div[1]")

            # Get the new content text
            new_content_text = [element.text for element in new_content_elements]

            # Get the new content length
            new_content_length = len(new_content_elements)

            # Assert that the content length remains the same
            assert initial_content_length == new_content_length, f"Expected {initial_content_length} elements, but got {new_content_length} elements."

            # Assert that the content has changed
            assert initial_content_text != new_content_text, "Expected the initial content to be different from the new content after reload."

            # Assert that each element's text has changed
            for i in range(initial_content_length):
                assert initial_content_text[i] != new_content_text[
                    i], f"Expected element {i} to have a different text, but it was the same."

            logger.info("Dynamic Content Test Passed")
        except:
            logger.error("Dynamic Content Test Failed")
            raise


