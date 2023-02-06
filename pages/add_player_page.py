import time

from pages.add_a_match_form import AddAMatchForm
from pages.base_page import BasePage


class AddPlayerPage(BasePage):
    add_player_page_title = "Add player"
    edit_player_page_title = "Edit player"
    page_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    email_xpath = "//input[@name='email']"
    name_xpath = "//input[@name='name']"
    surname_xpath = "//input[@name='surname']"
    phone_xpath = "//input[@name='phone']"
    weight_xpath = "//input[@name='weight']"
    height_xpath = "//input[@name='height']"
    age_xpath = "//input[@name='age']"
    leg_xpath = "//input[@id='leg']"
    leg_select_xpath = "//*[@id='mui-component-select-leg']"
    leg_clickable_xpath = "//input[@id='leg']/parent::div/div"
    leg_menu_right_xpath = "//*[@id='menu-leg']/div[3]/ul/li[1]"
    leg_menu_left_xpath = "//*[@id='menu-leg']/div[3]/ul/li[2]"
    club_xpath = "//input[@name='club']"
    level_xpath = "//input[@name='level']"
    main_position_xpath = "//input[@name='mainPosition']"
    second_position_xpath = "//input[@name='secondPosition']"
    district_xpath = "//input[@name='district']"
    district_clickable_xpath = "//input[@name='district']/parent::div/div"
    district_menu_silesia_xpath = "//*[@id='menu-district']/div[3]/ul/li[12]"
    district_menu_first_element_xpath = "//*[@id='menu-district']/div[3]/ul/li[1]"
    achievements_xpath = "// input[@name='achievements']"
    lang_arr_xpath = "//input[@name='languages["
    end_arr_xpath = "]']"
    web_laczy_xpath = "//input[@name='webLaczy']"
    web90_xpath = "// input[@name='web90']"
    webFB_xpath = "//input[@name='webFB']"
    webYT_arr_xpath = "//input[@name='webYT["

    add_lang_button_xpath = "//div[15]/button"
    add_link_to_youtube_button_xpath = "//div[19]/button"

    left_leg_text_en = "Left leg"
    left_leg_text_pl = "Lewa"
    district_silesia_en = "Silesia"

    submit_button_xpath = "//*[@type='submit']"
    page_title_xpath = "//form/div[1]/div/span"

    save_progress_xpath = "//*[@class='Toastify']/div"

    def type_in_email(self, value):
        self.field_send_keys(self.email_xpath, value)

    def type_in_name(self, value):
        self.field_send_keys(self.name_xpath, value)

    def type_in_surname(self, value):
        self.field_send_keys(self.surname_xpath, value)

    def type_in_phone(self, value):
        self.field_send_keys(self.phone_xpath, value)

    def type_in_weight(self, value):
        self.field_send_keys(self.weight_xpath, value)

    def type_in_height(self, value):
        self.field_send_keys(self.height_xpath, value)

    def type_in_age(self, value):
        self.field_send_keys(self.age_xpath, value)

    def select_leg(self, value):
        self.click_on_the_element(self.leg_clickable_xpath)
        if value == self.left_leg_text_en or value == self.left_leg_text_pl:
            self.click_on_the_element(self.leg_menu_left_xpath)
        else:
            self.click_on_the_element(self.leg_menu_right_xpath)

    def type_in_club(self, value):
        self.field_send_keys(self.club_xpath, value)

    def type_in_level(self, value):
        self.field_send_keys(self.level_xpath, value)

    def type_in_main_position(self, value):
        self.field_send_keys(self.main_position_xpath, value)

    def type_in_second_position(self, value):
        self.field_send_keys(self.second_position_xpath, value)

    def select_district(self, value):
        self.click_on_the_element(self.district_clickable_xpath)
        if value == self.district_silesia_en:
            self.wait_for_element_to_be_clickable(self.district_menu_silesia_xpath)
            self.click_on_the_element(self.district_menu_silesia_xpath)

    def type_in_achievements(self, value):
        self.field_send_keys(self.achievements_xpath, value)

    def add_languages(self, values):
        i = 0
        for value in values:
            self.click_on_the_element(self.add_lang_button_xpath)
            xpath = self.lang_arr_xpath + str(i) + self.end_arr_xpath
            self.wait_for_element_to_be_clickable(xpath)
            self.field_send_keys(xpath, value)
            i = i + 1

    def type_in_weblaczy(self, value):
        self.field_send_keys(self.web_laczy_xpath, value)

    def type_in_web90(self, value):
        self.field_send_keys(self.web90_xpath, value)

    def type_in_webfb(self, value):
        self.field_send_keys(self.webFB_xpath, value)

    def add_youtubes(self, values):
        i = 0
        for value in values:
            self.click_on_the_element(self.add_link_to_youtube_button_xpath)
            xpath = self.webYT_arr_xpath + str(i) + self.end_arr_xpath
            self.wait_for_element_to_be_clickable(xpath)
            self.field_send_keys(xpath, value)
            i = i + 1

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    @staticmethod
    def get_edit_page_title(edited_player):
        return AddPlayerPage.edit_player_page_title + " " + edited_player["name"] + " " + edited_player["surname"]

    def is_right_title(self, page_title):
        assert self.get_title_from_page(self.page_url) == page_title

    def is_sub_menu_player_exist(self):
        assert self.is_element_exist(AddAMatchForm.match_player_menu_xpath)

    def wait_for_save_be_complete(self, edited_player):
        self.wait_for_text_to_be_present_in_element(self.page_title_xpath, self.get_edit_page_title(edited_player))

    def required_sign_appear(self):
        self.visibility_of_element_located(self.required_mark_xpath)

    pass
