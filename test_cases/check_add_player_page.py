import time
import unittest

from pages.base_page import BasePage
from pages.dashboard import Dashboard
from pages.add_player_page import AddPlayerPage
from test_cases.login_to_the_system import TestLoginPage


class TestAddPlayerPage(unittest.TestCase):
    def setUp(self):
        TestLoginPage.login_to_the_system()
        dashboard_page = Dashboard()
        dashboard_page.click_add_player_button()
        add_player_page = AddPlayerPage()
        add_player_page.is_right_title(add_player_page.add_player_page_title)

    @staticmethod
    def fillPlayer(add_player_page, player_dictionary, file_name):
        BasePage.file_name = file_name
        if "email" in player_dictionary.keys():
            add_player_page.type_in_email(player_dictionary["email"])
        if "name" in player_dictionary.keys():
            add_player_page.type_in_name(player_dictionary["name"])
        if "surname" in player_dictionary.keys():
            add_player_page.type_in_surname(player_dictionary["surname"])
        if "phone" in player_dictionary.keys():
            add_player_page.type_in_phone(player_dictionary["phone"])
        if "weight" in player_dictionary.keys():
            add_player_page.type_in_weight(player_dictionary["weight"])
        if "height" in player_dictionary.keys():
            add_player_page.type_in_height(player_dictionary["height"])
        if "age" in player_dictionary.keys():
            add_player_page.type_in_age(player_dictionary["age"])
        if "leg" in player_dictionary.keys():
            add_player_page.select_leg(player_dictionary["leg"])
        if "club" in player_dictionary.keys():
            add_player_page.type_in_club(player_dictionary["club"])
        if "level" in player_dictionary.keys():
            add_player_page.type_in_level(player_dictionary["level"])
        if "mainPosition" in player_dictionary.keys():
            add_player_page.type_in_main_position(player_dictionary["mainPosition"])
        if "secondPosition" in player_dictionary.keys():
            add_player_page.type_in_second_position(player_dictionary["secondPosition"])
        if "district" in player_dictionary.keys():
            add_player_page.select_district(player_dictionary["district"])
        if "achievements" in player_dictionary.keys():
            add_player_page.type_in_achievements(player_dictionary["achievements"])
        if "languages" in player_dictionary.keys():
            add_player_page.add_languages(player_dictionary["languages"])
        if "webLaczy" in player_dictionary.keys():
            add_player_page.type_in_weblaczy(player_dictionary["webLaczy"])
        if "web90" in player_dictionary.keys():
            add_player_page.type_in_web90(player_dictionary["web90"])
        if "webFB" in player_dictionary.keys():
            add_player_page.type_in_webfb(player_dictionary["webFB"])
        if "youtubes" in player_dictionary.keys():
            add_player_page.add_youtubes(player_dictionary["youtubes"])

    def test_add_player_with_max_info(self):
        new_player_max_info = {"email": "player01@getnada.com",
                               "name": "Player01Name",
                               "surname": "Player01Surname",
                               "phone": "player01Phone",
                               "weight": "70",
                               "height": "190",
                               "age": "02/25/1990",
                               "leg": "Right leg",
                               "club": "Player01Club",
                               "level": "player01Level",
                               "mainPosition": "player01MainPosition",
                               "secondPosition": "player01SecondPosition",
                               "district": "Silesia",
                               "achievements": "player01Achievements",
                               "languages": ["Polish", "English"],
                               "webLaczy": "ProfilePlayer01LNP",
                               "web90": "ProfilePlayer0190M",
                               "webFB": "NicknamePlayer01FB",
                               "youtubes": ["https://www.youtube.com/@test1", "https://www.youtube.com/@test2"]
                               }

        add_player_page = AddPlayerPage()
        self.fillPlayer(add_player_page, new_player_max_info, "d:\ScreenShots\TC_PP_01.png")
        add_player_page.click_submit_button()
        add_player_page.wait_for_save_be_complete(new_player_max_info)
        add_player_page.is_sub_menu_player_exist()

    def test_add_player_with_min_info(self):
        new_player_min_info = {"name": "PlayerMin01Name",
                               "surname": "PlayerMin01Surname",
                               "age": "02/25/1990",
                               "mainPosition": "playerMin01MainPosition"
                               }

        add_player_page = AddPlayerPage()
        self.fillPlayer(add_player_page, new_player_min_info, "d:\ScreenShots\TC_PP_02.png")
        add_player_page.click_submit_button()
        add_player_page.wait_for_save_be_complete(new_player_min_info)

    def test_add_player_no_all_required_info(self):
        player_info = {"name": "PlayerNoSave01Name",
                       "surname": "PlayerNoSave01Surname"
                       }

        add_player_page = AddPlayerPage()
        self.fillPlayer(add_player_page, player_info, "d:\ScreenShots\TC_PP_03.png")
        add_player_page.click_submit_button()
        add_player_page.click_submit_button()
        add_player_page.required_sign_appear()
        add_player_page.is_right_title(add_player_page.add_player_page_title)

    @classmethod
    def tearDown(cls):
        BasePage.shared_driver.save_screenshot(BasePage.file_name)
        time.sleep(3)
        BasePage.tear_down()
