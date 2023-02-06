
from pages.base_page import BasePage


class Dashboard(BasePage):
    page_title = "Scouts panel"

    main_page_menu_xpath = "//div[@role='presentation']/ul[1]/div[1]"
    players_menu_xpath = "//div[@role='presentation']/ul[1]/div[2]"
    language_menu_xpath = "//div[@role='presentation']/ul[2]/div[1]"
    sign_out_menu_xpath = "//div[@role='presentation']/ul[2]/div[2]"

    players_count_value_xpath = "(//main//b)[1]"
    matches_count_value_xpath = "(//main//b)[2]"
    reports_count_value_xpath = "(//main//b)[3]"
    events_count_value_xpath = "(//main//b)[4]"

    dev_team_contact_link_xpath = "//span[text()='Dev team contact']/parent::a"
    add_player_button_xpath = "(//div[@class='MuiCardContent-root'])[2]/a/button"
    last_created_player_link_xpath = "(//div[@class='MuiCardContent-root'])[3]/a[1]"
    last_updated_player_link_xpath = "(//div[@class='MuiCardContent-root'])[3]/a[2]"
    last_created_match_link_xpath = "(//div[@class='MuiCardContent-root'])[3]/a[3]"
    last_updated_match_link_xpath = "(//div[@class='MuiCardContent-root'])[3]/a[4]"
    last_updated_report_link_xpath = "(//div[@class='MuiCardContent-root'])[3]/a[5]"

    def is_right_title(self):
        self.wait_for_element_to_be_clickable(self.add_player_button_xpath)
        assert self.get_title_from_page(self.page_url) == self.page_title

    def click_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    # Xpath for english version of site
    #   players_count_value_eng_xpath = "//*[text()='Players count']//following-sibling::div/b"
    #   matches_count_value_eng_xpath = "//*[text()='Matches count']//following-sibling::div/b"
    #   reports_count_value_eng_xpath = "//*[text()='Reports count']//following-sibling::div/b"
    #   events_count_value_eng_xpath = "//*[text()='Events count']//following-sibling::div/b"
    #   add_player_button_eng_xpath = "//span[text()='Add player']/parent::button"
    #   last_created_player_link_eng_xpath = "//*[text()='Last created player']//following-sibling::a"
    #   last_updated_player_link_eng_xpath = "//*[text()='Last updated player']//following-sibling::a"
    #   last_created_match_link_eng_xpath = "//*[text()='Last created match']//following-sibling::a"
    #   last_updated_match_link_eng_xpath = "//*[text()='Last updated match']//following-sibling::a"
    #   last_updated_report_link_eng_xpath = "//*[text()='Last updated report']//following-sibling::a"

    pass
