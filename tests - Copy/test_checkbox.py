import pytest

from pageObjects.checkbox_page import CheckboxPage
from utilities.logging_utility import create_logger

logger = create_logger(__name__, "test_checkboxes.log", "pass" or "fail")


@pytest.mark.checkboxes
class TestCheckboxes:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.page = CheckboxPage(browser)
        self.page.load()
        logger.info("Checkbox setup Successful")

    def test_checkbox1_checked(self):
        assert not self.page.checkbox1_checked()
        self.page.check_checkbox1()
        assert self.page.checkbox1_checked()
        logger.info("TestCheckbox1Checked Successful")

    def test_checkbox2_unchecked(self):
        assert self.page.checkbox2_checked()
        self.page.uncheck_checkbox2()
        assert not self.page.checkbox2_checked()
        logger.info("Test Checkbox2 Unchecked Successful")
