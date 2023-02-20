import time
import unittest

from pages.base_page import BasePage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage


class TestLoginPage(unittest.TestCase):
    user = {"login": 'user01@getnada.com', "password": 'Test-1234'}

    @staticmethod
    def fill_user(user_login, data, file_name):
        BasePage.file_name = file_name
        user_login.is_right_title()
        user_login.type_in_email(data["login"])
        user_login.fill_password(data["password"])
        user_login.click_login_button()

    @staticmethod
    def login_to_the_system():
        user_login = LoginPage()
        TestLoginPage.fill_user(user_login, TestLoginPage.user, "d:\ScreenShots\TC_LP_01.png")

    def test_login_to_the_system(self):
        self.login_to_the_system()
        dashboard_page = Dashboard()
        dashboard_page.is_right_title()

    def test_empty_login(self):
        user_login = LoginPage()
        user = {"login": '', "password": 'Test-1234'}
        self.fill_user(user_login, user, "d:\ScreenShots\TC_LP_02.png")

        self.assertEqual(user_login.get_element_text_or_empty_str(user_login.error_xpath),
                         user_login.empty_login_error_text_en)

    def test_empty_password(self):
        user_login = LoginPage()
        user = {"login": 'user01@getnada.com', "password": ''}
        self.fill_user(user_login, user, "d:\ScreenShots\TC_LP_03.png")

        self.assertEqual(user_login.get_element_text_or_empty_str(user_login.error_xpath),
                         user_login.empty_password_error_text_en)

    def test_incorrect_login_data(self):
        user_login = LoginPage()
        user = {"login": 'incorrect@gmail.com', "password": 'incorrectpass'}
        self.fill_user(user_login, user, "d:\ScreenShots\TC_LP_04.png")

        self.assertEqual(user_login.get_element_text_or_empty_str(user_login.error_xpath),
                         user_login.incorrect_data_error_text_en)

    @classmethod
    def tearDown(cls):
        BasePage.shared_driver.save_screenshot(BasePage.file_name)
        time.sleep(3)
        BasePage.tear_down()
