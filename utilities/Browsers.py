from selenium import webdriver

from selenium.webdriver.chrome.service import Service
# --Chrome
#service_obj = Service("C:/Driver_Chrome/chromedriver_win32/chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)

# avoid crashing Chrome after lunch
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
#----------------------------------------------------------------------------------

# --Firefox
service_obj = Service("C:/Driver_Gecko/geckodriver-v0.32.2-win32/geckodriver.exe");
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
#-----------------------------------------------------------------------------------

# --Microsoft Edge
service_obj = Service("C:/Driver_Edge/edgedriver_win32/msedgedriver.exe");
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options)
#-----------------------------------------------------------------------------------




driver.maximize_window()
driver.get("https://courses.rahulshettyacademy.com/courses")
print(driver.title)
print(driver.current_url)
driver.forward()
driver.back()
driver.refresh()
driver.forward()
driver.close()













