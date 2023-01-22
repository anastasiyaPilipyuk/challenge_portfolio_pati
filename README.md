## Task 1: software configuration.
### Subtask 1: Why did I choose to participate in the Dare IT Challenge?
I've decided to take a participate in this project for 
 - obtaining new knowledge,
 - finding extremely interesting work,
 - just for having fun.

I hope all my expectations will come true :blush:

## TASK 2: selectors

**header_xpath**
 + //*[@id="__next"]/form/div/div[1]/h5
 + //*[text()="Scouts Panel"]
 + //child::div/h5

**login_label_xpath**
 - //*[@id="login-label"]
 - //label[@for="login"]
 - //child::div/label

**login_input_xpath**
 - //*[@id="login"]
 - //input[@type="text"]
 - //child::div/input

**password_label_xpath**
 - //*[@id="password-label"]
 - //label[@for="password"]
 - //child::div[2]/label

**password_input_xpath**
 - //*[@id="password"]
 - //input[@type="password"]
 - //child::div[2]/div/input

**error_span_xpath**
 - //*[@id="__next"]/form/div/div[1]/div[3]/span
 - //*[text()="Please provide your username or your e-mail."]
 - //*[text()="Identifier or password invalid."]
 - //*[text()="Too many attempts, please try again in a minute."]
 - //child::div/span

**remaind_password_hyperlink_xpath**
 - //*[@id="__next"]/form/div/div[1]/a
 - //*[text()="Remind password"]
 - //*[text()="Przypomnij hasło"]
 - //child::div/a

**current_language_div_xpath**
 - //*[@id="__next"]/form/div/div[2]/div/div
 - //*[contains(@class,"MuiSelect-selectMenu")]
 - //child::div[2]/div/div

**select_language_input_xpath**
 - //*[@id="__next"]/form/div/div[2]/div/input
 - //input[@value="en"]
 - //input[@value="pl"]
 - //*[contains(@class,"MuiSelect-nativeInput")]

**select_language_list_xpath**
 - //*[@id="menu-"]/div[3]/ul
 - //*[contains(@class,"MuiList-root")]
 - //child::ul

**select_language_list_polski_xpath**
 - //*[@id="menu-"]/div[3]/ul/li[1]
 - //li[@data-value="pl"]
 - //child::li

**select_language_list_english_xpath**
 - //*[@id="menu-"]/div[3]/ul/li[2]
 - //li[@data-value="en"]
 - //child::li[2]

**sign_in_button_xpath**
 - //*[@id="__next"]/form/div/div[2]/button
 - //button[@type="submit"]
 - //child::div[2]/button