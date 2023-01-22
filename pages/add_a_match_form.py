from pages.base_page import BasePage


class AddAMatchForm(BasePage):
    main_page_menu_xpath = "//div[@role='presentation']/ul[1]/div[1]"
    players_menu_xpath = "//div[@role='presentation']/ul[1]/div[2]"

    match_player_menu_xpath = "//div[@role='presentation']/ul[2]/div[1]"
    matches_menu_xpath = "//div[@role='presentation']/ul[2]/div[2]"
    reports_menu_xpath = "//div[@role='presentation']/ul[2]/div[3]"

    language_menu_xpath = "//div[@role='presentation']/ul[3]/div[1]"
    sign_out_menu_xpath = "//div[@role='presentation']/ul[3]/div[2]"

    my_team_input_xpath = "//input[@name='myTeam']"
    enemy_team_input_xpath = "//input[@name='enemyTeam']"
    my_team_score_input_xpath = "//input[@name='myTeamScore']"
    enemy_team_score_input_xpath = "//input[@name='enemyTeamScore']"
    date_input_xpath = "//input[@name='date']"
    match_at_home_radio_xpath = "//input[@name='matchAtHome' and @value='true']"
    match_out_home_radio_xpath = "//input[@name='matchAtHome' and @value='false']"
    tshirt_input_xpath = "//input[@name='tshirt']"
    league_input_xpath = "//input[@name='league']"
    time_played_input_xpath = "//input[@name='timePlayed']"
    number_input_xpath = "//input[@name='number']"
    web_match_input_xpath = "//input[@name='webMatch']"
    general_input_xpath = "//input[@name='general']"
    rating_input_xpath = "//input[@name='rating']"

    submit_button_xpath = "//button[@type='submit']"
    clear_button_xpath = "//*[text()='Clear']/parent::button"

    pass
