import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utilities.logging_utility import create_logger
from selenium.common.exceptions import NoSuchElementException

logger = create_logger(__name__, "test_login.log", "pass" or "fail")

@pytest.mark.login_success
class TestLoginSuccess:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        try:
            # Navigate to the login page
            browser.get("http://localhost:7080/login")

            # Find the username and password fields
            self.username_field = browser.find_element(By.ID, "username")
            self.password_field = browser.find_element(By.ID, "password")

            # Enter the correct login credentials
            self.username_field.send_keys("tomsmith")
            self.password_field.send_keys("SuperSecretPassword!")

            # Submit the login form
            self.password_field.submit()

            # Wait time seconds
            time.sleep(2)

            logger.info("Login Success Setup Successful")
        except:
            logger.error("Login Success Setup Failed")
            raise

    def test_login_success_message(self, browser):
        try:
            # Assert that the success message is displayed
            success_message = browser.find_element(By.CSS_SELECTOR, '.flash.success')
            assert "You logged into a secure area!" in success_message.text
            logger.info("Login Success Test Passed")
        except NoSuchElementException:
            logger.error("Login Success Test Failed - Element not found")
            raise
        except AssertionError:
            logger.error("Login Success Test Failed - Assertion Error")
            raise
