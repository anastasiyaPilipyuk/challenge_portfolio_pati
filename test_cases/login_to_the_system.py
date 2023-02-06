import time
import unittest

from pages.base_page import BasePage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage


class TestLoginPage(unittest.TestCase):
    user = {"login": 'user01@getnada.com', "password": 'Test-1234'}

    def test_login_to_the_system(self):
        user_login = LoginPage()
        user_login.is_right_title()
        user_login.assert_element_text(user_login.header_xpath, "Scouts Panel")
        user_login.type_in_email(TestLoginPage.user["login"])
        user_login.fill_password(TestLoginPage.user["password"])
        user_login.click_login_button()

        dashboard_page = Dashboard()
        dashboard_page.is_right_title()
        user_login.save_screenshot("d:\ScreenShots\TC_LP_01.png")

    def test_empty_login(self):
        user_empty_login = {"login": '', "password": 'Test-1234'}
        user_login = LoginPage()
        user_login.is_right_title()
        user_login.assert_element_text(user_login.header_xpath, "Scouts Panel")
        user_login.type_in_email(user_empty_login["login"])
        user_login.fill_password(user_empty_login["password"])
        user_login.click_login_button()
        self.assertEqual(user_login.get_element_text_or_empty_str(user_login.error_xpath),
                         user_login.empty_login_error_text_en)
        user_login.save_screenshot("d:\ScreenShots\TC_LP_02.png")

    def test_empty_password(self):
        user_empty_password = {"login": 'user01@getnada.com', "password": ''}
        user_login = LoginPage()
        user_login.is_right_title()
        user_login.assert_element_text(user_login.header_xpath, "Scouts Panel")
        user_login.type_in_email(user_empty_password["login"])
        user_login.fill_password(user_empty_password["password"])
        user_login.click_login_button()
        self.assertEqual(user_login.get_element_text_or_empty_str(user_login.error_xpath),
                         user_login.empty_password_error_text_en)
        user_login.save_screenshot("d:\ScreenShots\TC_LP_03.png")

    def test_incorrect_login_data(self):
        user_incorrect_data = {"login": 'incorrect@gmail.com', "password": 'incorrectpass'}
        user_login = LoginPage()
        user_login.is_right_title()
        user_login.assert_element_text(user_login.header_xpath, "Scouts Panel")
        user_login.type_in_email(user_incorrect_data["login"])
        user_login.fill_password(user_incorrect_data["password"])
        user_login.click_login_button()
        self.assertEqual(user_login.get_element_text_or_empty_str(user_login.error_xpath),
                         user_login.incorrect_data_error_text_en)
        user_login.save_screenshot("d:\ScreenShots\TC_LP_04.png")


    @classmethod
    def tearDown(cls):
        time.sleep(3)
        BasePage.tear_down()
