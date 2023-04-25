import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        #options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        service_obj = Service("C:/Driver_Gecko/geckodriver-v0.32.2-win32/geckodriver.exe");
        options = webdriver.FirefoxOptions()
        #options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    elif browser_name == "edge":
        service_obj = Service("C:/Driver_Edge/edgedriver_win32/msedgedriver.exe");
        options = webdriver.EdgeOptions()
        #options.add_argument("--headless")
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError("Invalid browser name")

    driver.implicitly_wait(4)

    yield driver

    # Quit the WebDriver instance after the test
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name, item.funcargs["browser"])
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name, browser):
    browser.get_screenshot_as_file(name)
