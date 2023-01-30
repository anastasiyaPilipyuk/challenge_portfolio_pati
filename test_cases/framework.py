import unittest

from pages.base_page import BasePage
from pages.login_page import LoginPage


class Test(unittest.TestCase):

    def test_title(self):
        user_login = LoginPage()
        actual_title = user_login.get_title_from_page()
        expected_title = 'Scouts panel - sign in'
        assert actual_title == expected_title
        BasePage.tear_down()

    # Element of the first task: Try to search the Internet yourself how to get rid of the error:
    # "DeprecationWarning: executable_path has been deprecated, please pass in a Service object"


