from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utilities.logging_utility import create_logger

logger = create_logger(__name__, "test_file_upload.log", "pass" or "fail")


class TestFileUpload:

    def test_file_upload(self, browser):
        # Navigate to the File Upload page
        browser.get("http://localhost:7080/upload")

        # Find the file input field and upload a file
        file_input = browser.find_element(By.ID, "file-upload")
        file_input.send_keys("C:\\Users\\acade\\PycharmProjects\\Dotdashcom_test_PYTHON\\test.txt")

        # Click the upload button
        upload_button = browser.find_element(By.ID, "file-submit").click()

        # Wait for the upload to finish and check the uploaded file name
        try:
            WebDriverWait(browser, 5).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#uploaded-files"), "test.txt"))
            assert "test.txt" in browser.find_element(By.CSS_SELECTOR, "#uploaded-files").text
            # Log a success message
            logger.info("File Upload Passed")

        except:
            # Log an error message and re-raise the exception
            logger.error("File Upload Failed")
            raise

            # Wait time seconds
        time.sleep(2)
