from pages.base_page import BasePage


class LoginPage(BasePage):
    page_title = "Scouts panel - sign in"

    header_xpath = "//h5"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    error_xpath = "//div[3]/span"
    empty_login_error_text_en = "Please provide your username or your e-mail."
    empty_password_error_text_en = "Please provide your password."
    incorrect_data_error_text_en = "Identifier or password invalid."

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def fill_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_login_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def is_right_title(self):
        assert self.get_title_from_page() == self.page_title
