from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logging_utility import create_logger

logger = create_logger(__name__, "test_java_scripts_alerts.log", "pass" or "fail")

class TestJavaScriptAlerts:

    def test_js_alert(self, browser):
        try:
            # Navigate to the JavaScript Alerts page
            browser.get("http://localhost:7080/javascript_alerts")

            # Click the "Click for JS Alert" button
            alert_button = browser.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

            # Switch to the alert and get its message
            alert_text = browser.switch_to.alert.text;
            browser.switch_to.alert.accept()

            # Assert the alert message
            assert alert_text == "I am a JS Alert"

            # Log a success message
            logger.info("TestJavaScriptAlerts test_js_alert Passed")

        except:
            # Log an error message and re-raise the exception
            logger.error("TestJavaScriptAlerts test_js_alert Failed")
            raise


    def test_js_confirm(self, browser):
        try:
            # Navigate to the JavaScript Alerts page
            browser.get("http://localhost:7080/javascript_alerts")

            # Click the "Click for JS Confirm" button
            confirm_button = browser.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()

            # Switch to the alert and get its message
            alert_text = browser.switch_to.alert.text;
            browser.switch_to.alert.accept()

            # Assert the alert message
            assert alert_text == "I am a JS Confirm"

            # Log a success message
            logger.info("TestJavaScriptAlerts test_js_confirm Passed")

        except:
            # Log an error message and re-raise the exception
            logger.error("TestJavaScriptAlerts test_js_confirm Failed")
            raise


    def test_js_prompt(self, browser):
        try:
            # Navigate to the JavaScript Alerts page
            browser.get("http://localhost:7080/javascript_alerts")

            # Click the "Click for JS Prompt" button
            prompt_button = browser.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()

            # Switch to the alert, type a message, and click OK
            browser.switch_to.alert.send_keys("HELLO VLAD");
            browser.switch_to.alert.accept()

            # Wait for the result to appear
            result = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.ID, "result"))
            )

            # Assert that the result contains the typed message
            assert "HELLO VLAD" in result.text

            # Log a success message
            logger.info("TestJavaScriptAlerts test_js_prompt Passed")

        except:
            # Log an error message and re-raise the exception
            logger.error("TestJavaScriptAlerts test_js_prompt Failed")
            raise
