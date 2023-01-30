from pages.base_page import BasePage


class AddPlayerPage(BasePage):
    page_title = "Add player"
    page_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"

    def is_right_title(self):
        assert self.get_title_from_page(self.page_url) == self.page_title

    pass
