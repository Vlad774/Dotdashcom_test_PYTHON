import pytest
from pageObjects.context_menu_page import ContextMenuPage
from utilities.logging_utility import create_logger


logger = create_logger(__name__, "test_context_menu.log", "pass" or "fail")

@pytest.mark.context_menu
class TestContextMenu:


    def test_context_menu_alert(self, browser):
        context_menu_page = ContextMenuPage(browser)
        try:
            # Navigate to the context menu page
            browser.get("http://localhost:7080/context_menu")
            logger.info("Context Menu Setup Successful")

            context_menu_page.right_click_box()

            # Switch to the alert and get its text
            alert = browser.switch_to.alert
            alert_text = alert.text
            alert.accept()

            # Assert that the alert text contains the expected string
            assert "You selected a context menu" in alert_text
            logger.info("Context Menu Test Passed")
        except:
            logger.error("Context Menu Test Failed")
            raise
