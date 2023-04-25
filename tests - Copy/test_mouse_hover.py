from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logging_utility import create_logger

logger = create_logger(__name__, "test_mouse_hover.log", "pass" or "fail")

class TestMouseHover:

    def test_mouse_hover(self, browser):
        try:
            # Navigate to the Mouse Hover page
            browser.get("http://localhost:7080/hovers")

            # Find all the images
            images = browser.find_elements(By.TAG_NAME, "/img/avatar-blank.jpg")

            # Loop through the images and hover over each one
            for image in images:
                # Wait for the image to be clickable
                WebDriverWait(browser, 3).until(
                    EC.element_to_be_clickable((By.XPATH, "/img/avatar-blank.jpg"))
                )

                # Move the mouse over the image
                actions = ActionChains(browser)
                actions.move_to_element(image)
                actions.perform()

                # Wait for the overlay to be displayed
                WebDriverWait(browser, 3).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "figcaption"))
                )

                # Assert that the overlay is displayed
                assert browser.find_element(By.CLASS_NAME, "figcaption").is_displayed()

            # Log a success message
            logger.info("TestMouseHover Passed")

        except:
            # Log an error message and re-raise the exception
            logger.error("TestMouseHover Failed")
            raise

