import os
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT, DEFAULT_LOCATOR_TYPE


class BasePage:
    page_title = ""
    page_url = "https://scouts.futbolkolektyw.pl/en/"
    # page_url = "https://scouts-test.futbolkolektyw.pl/"
    shared_driver = None

    required_mark_xpath = "//*[text()='Required']"
    file_name = "d:\ScreenShots\TC_LP_01.png"

    @classmethod
    def set_up(cls):
        if BasePage.shared_driver is None:
            os.chmod(DRIVER_PATH, 755)
            BasePage.shared_driver_service = Service(executable_path=DRIVER_PATH)
            BasePage.shared_driver = webdriver.Chrome(service=BasePage.shared_driver_service)
            BasePage.shared_driver.get(cls.page_url)
            BasePage.shared_driver.fullscreen_window()
            BasePage.shared_driver.implicitly_wait(IMPLICITLY_WAIT)
        return BasePage.shared_driver

    @classmethod
    def tear_down(cls):
        if BasePage.shared_driver is not None:
            BasePage.shared_driver.quit()
            BasePage.shared_driver = None

    def __init__(self):
        self.driver = self.set_up()

    def field_send_keys(self, selector, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(self, selector, selector_type=By.XPATH):
        return self.driver.find_element(selector_type, selector).click()

    def get_title_from_page(self, url=page_url):
        self.driver.get(url)
        return self.driver.title

    def assert_element_text(self, xpath, expected_text):
        """Comparing expected text with observed value from web element

           :param xpath: xpath to element with text to be observed
           :param expected_text: text what we expecting to be found
           :return: None
       """
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        element_text = element.text
        assert expected_text == element_text

    def wait_for_element_to_be_clickable(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        time.sleep(1)

    def wait_for_text_to_be_present_in_element(self, locator, text, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.text_to_be_present_in_element((locator_type, locator), text))
        time.sleep(1)

    def visibility_of_element_located(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((locator_type, locator)))
        time.sleep(1)

    def is_element_exist(self, selector, locator_type=DEFAULT_LOCATOR_TYPE):
        element = self.driver.find_element(locator_type, selector)
        if element is None:
            return False
        return True

    def get_element_text_or_empty_str(self, selector, locator_type=DEFAULT_LOCATOR_TYPE):
        element = self.driver.find_element(locator_type, selector)
        if element is None:
            return ''
        return element.text

#    def save_screenshot_(self, file_name):
#       self.driver.save_screenshot(file_name)
