from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import  Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import pytest

GridUrl = "http://localhost:4444/wd/hub"

def get_browser_config(browser_name):
    if browser_name =="chrome_win":
        lt_options = {"username": "simhachalampanasa",
                      "accessKey": "LT_G4qA3tMPBsrIOa5ecdKdEmsaveEMJfJV4SEniYLClkLmgFD"}
        options = ChromeOptions()
        options.set_capability("browserVersion","137.0")
        options.set_capability("platformName", "Windows 10")
        #options.platform_name = "Windows 10"
        options.set_capability("NetworkLogsEnabled", True)
        options.set_capability("ConsoleLogEnabled", True)
        options.set_capability("VideoRecorderEnabled", True)
        options.set_capability("ScreenshotEnabled", True)

        return options

    elif browser_name =="edge_mac":
        lt_options = {"username": "simhachalampanasa",
                      "accessKey": "LT_G4qA3tMPBsrIOa5ecdKdEmsaveEMJfJV4SEniYLClkLmgFD"}
        options = EdgeOptions()
        options.set_capability("browserVersion", "137.0")
        options.set_capability("platformName", "macOS Sierra")
        options.set_capability("NetworkLogsEnabled", True)
        options.set_capability("ConsoleLogEnabled", True)
        options.set_capability("VideoRecorderEnabled", True)
        options.set_capability("ScreenshotEnabled", True)
        return options

    else:
        raise Exception("Invalid browser config")
    return caps

@pytest.fixture(params=["chrome_win","edge_mac"], scope="class")
def driver(request):
    options = get_browser_config(request.param)
    driver = webdriver.Remote(command_executor=GridUrl,options=options)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()