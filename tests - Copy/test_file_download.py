import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logging_utility import create_logger

logger = create_logger(__name__, "test_file_download.log", "pass" or "fail")

class TestFileDownload:

    def test_file_download(self, browser):
        try:
            # Navigate to the File Download page
            browser.get("http://localhost:7080/download")

            # Find and click the file link
            file_link = browser.find_element(By.CSS_SELECTOR, ".example a").click()

            # Wait for the file to download
            WebDriverWait(browser, 10).until(EC.url_contains("download"))
            # Wait 3 seconds
            time.sleep(3)

            # Assert that the file has been downloaded
            assert "some-file.txt" in browser.page_source

            # Log a success message
            logger.info("TestFileDownload Passed")

        except:
            # Log an error message and re-raise the exception
            logger.error("TestFileDownload Failed")
            raise

