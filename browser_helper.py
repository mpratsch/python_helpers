from platform import system
from os import path

from selenium.webdriver import Chrome, ChromeOptions, DesiredCapabilities, Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import (
    TimeoutException,
    JavascriptException,
    StaleElementReferenceException,
    NoSuchElementException,
)


GECKODRIVER_VERSION = "v0.28.0"
EXE_MAIN_DIR = f"/mnt/c/MyApps/"
HOME_DIR = path.expanduser("~")


class BrowserHelper:
    def __init__(self, headless=False):
        self.headless = headless
        # self.browser = browser
        # if browser.lower() == 'firefox':
        #    init_firefox(headless)

    def firefox(self):
        """Firefox Settings. Return firefox driver."""
        # zip_file_name = f"geckodriver-{GECKODRIVER_VERSION}-win64.zip"
        # download_url = f"https://github.com/mozilla/geckodriver/releases/download/{GECKODRIVER_VERSION}/{zip_file_name}"
        exe_file_name = "geckodriver.exe"
        exe_full_path = f"{EXE_MAIN_DIR}{exe_file_name}"
        # check_driver(exe_full_path=exe_full_path, zip_file_name=zip_file_name, download_url=download_url,)
        service_log_path = f"{HOME_DIR}/"
        if system() == "Windows":
            service_log_path = f"{HOME_DIR}\\Documents\\"
        ff_binary = FirefoxBinary(
            "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
        )
        ff_options = Options()
        ff_options.headless = self.headless  # Keeps it in the background
        # ff_options.log.level = "trace"
        ff_caps = DesiredCapabilities().FIREFOX
        # ff_caps["pageLoadStrategy"] = "none"
        firefox_driver = Firefox(
            firefox_binary=ff_binary,
            executable_path=exe_full_path,
            options=ff_options,
            capabilities=ff_caps,
            service_log_path=f"{service_log_path}geckodriver_aws-close-account.log",
        )
        return firefox_driver

    def chrome(self):
        """Chromedriver settings. Return chrome driver."""
        zip_file_name = "chromedriver_win32.zip"
        download_url = f"https://chromedriver.storage.googleapis.com/{CHROMEDRIVER_VERSION}/{zip_file_name}"
        exe_file_name = "chromedriver.exe"
        exe_full_path = f"{EXE_MAIN_DIR}{exe_file_name}"
        check_browser_driver(
            exe_full_path=exe_full_path,
            zip_file_name=zip_file_name,
            download_url=download_url,
        )

        ch_options = ChromeOptions()
        ch_options.add_experimental_option("useAutomationExtension", False)
        ch_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        ch_options.add_argument("--disable-extensions")
        if self.headless:
            ch_options.add_argument("--headless")  # Keeps it in the background
        ch_caps = DesiredCapabilities.CHROME
        ch_caps["pageLoadStrategy"] = "none"
        chrome_driver = Chrome(
            options=ch_options,
            executable_path=f"{exe_full_path}",
            desired_capabilities=ch_caps,
        )
        return chrome_driver
