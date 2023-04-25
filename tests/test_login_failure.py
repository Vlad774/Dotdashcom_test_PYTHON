import pytest
import time
from selenium.webdriver.common.by import By
from pageObjects.login_failure_page import LoginFailurePage
from utilities.logging_utility import create_logger

logger = create_logger(__name__, "test_login_failure.log", "pass" or "fail")

@pytest.mark.login_failure
class TestLoginFailure:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        try:
            # Navigate to the login page
            browser.get("http://localhost:7080/login")
            # Find the username and password fields
            self.username_field = browser.find_element(By.ID, "username")
            self.password_field = browser.find_element(By.ID, "password")
            # Enter incorrect login credentials
            self.username_field.send_keys("wrongusername")
            self.password_field.send_keys("wrongpassword")
            # Submit the login form
            self.password_field.submit()
            # Wait for 2 seconds
            time.sleep(2)
            logger.info("Login Failure Setup Successful")
        except:
            logger.error("Login Failure Setup Failed")
            raise

    def test_login_failure_message(self, browser):
        try:
            # Assert that the failure message is displayed
            login_failure_page = LoginFailurePage(browser)
            assert "Your username is invalid!" in login_failure_page.get_failure_message() or "Your password is invalid!" in login_failure_page.get_failure_message()
            logger.info("Login Failure Test Passed")
        except:
            logger.error("Login Failure Test Failed")
            raise
