from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logging_utility import create_logger

logger = create_logger(__name__, "test_notification_message.log", "pass" or "fail")

class TestNotificationMessage:

    def test_notification_message(self, browser):
        try:
            # Navigate to the Notification Message page
            browser.get("http://localhost:7080/notification_message_rendered")

            # Click the link multiple times and get the resulting message
            message = ""
            for i in range(3):
                link = browser.find_element(By.XPATH, "//a[contains(@href, '/notification_message')]").click()

                # Wait for the notification message to appear
                wait = WebDriverWait(browser, 10)
                message_elem = wait.until(EC.presence_of_element_located((By.ID, "flash")))
                message = message_elem.text

                # Check if the message contains any of the expected strings
                if "Action Successful" in message or "Action unsuccessful, please try again" in message or "Action Unsuccessful" in message:
                    break

            # Verify that the message is not empty
            assert message != ""

            # Log the test result
            if "Action Successful" in message:
                logger.info("TestNotificationMessage Passed: Action Successful message displayed")
            else:
                logger.warning("TestNotificationMessage Passed with Warning: Action unsuccessful message displayed")

        except:
            # Log an error message and re-raise the exception
            logger.error("TestNotificationMessage Failed")
            raise

        print("Notification Message Test Completed")
