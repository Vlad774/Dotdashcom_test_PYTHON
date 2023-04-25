import pytest
from selenium.webdriver import ActionChains

from pageObjects.drag_and_drop_page import DragAndDropPage
from utilities.logging_utility import create_logger


logger = create_logger(__name__, "test_drag_and_drop.log", "pass" or "fail")

@pytest.mark.drag_and_drop
class TestDragAndDrop:

    def test_drag_and_drop(self, browser):
        try:
            # Create a DragAndDropPage object
            page = DragAndDropPage(browser)

            # Navigate to the drag and drop page
            page.open()

            # Find the source and target elements using the page object
            source_element = page.source_element
            target_element = page.target_element

            # Perform the drag and drop action
            action = ActionChains(browser)
            action.drag_and_drop(source_element, target_element).perform()

            # Assert that the elements have been swapped
            assert target_element.text == "B"
            assert source_element.text == "A"

            logger.info("Drag and Drop Test Passed")
        except:
            logger.error("Drag and Drop Test Failed")
            raise
