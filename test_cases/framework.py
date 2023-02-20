import unittest

from pages.base_page import BasePage
from pages.login_page import LoginPage


class Test(unittest.TestCase):

    def test_title(self):
        user_login = LoginPage()
        actual_title = user_login.get_title_from_page()
        expected_title = 'Scouts panel - sign in'
        user_login.assert_element_text(user_login.header_xpath, "Scouts Panel")
        # user_login.assert_element_text(user_login.header_xpath, "PANEL SKAUTINGOWY")
        BasePage.file_name = "d:\ScreenShots\TC_DP_01.png"
        assert actual_title == expected_title

    @classmethod
    def tearDown(cls):
        BasePage.shared_driver.save_screenshot(BasePage.file_name)
        BasePage.tear_down()

    # Element of the first task: Try to search the Internet yourself how to get rid of the error:
    # "DeprecationWarning: executable_path has been deprecated, please pass in a Service object"
