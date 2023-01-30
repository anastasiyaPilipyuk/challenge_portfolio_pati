import unittest

from pages.base_page import BasePage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.add_player_page import AddPlayerPage


class TestAddPlayerPage(unittest.TestCase):
    user = {"login": 'user01@getnada.com', "password": 'Test-1234'}

    def test_add_player(self):
        user_login = LoginPage()
        user_login.is_right_title()
        user_login.type_in_email(self.user["login"])
        user_login.fill_password(self.user["password"])
        user_login.click_login_button()

        dashboard_page = Dashboard()
        dashboard_page.is_right_title()
        dashboard_page.click_add_player_button()

        add_player_page = AddPlayerPage()
        add_player_page.is_right_title()

        BasePage.tear_down()

    pass
