from behave import given, when, then


@given('Open the login page')
def open_login_page(context):
    context.app.login_page.open_login_page()


@then('Log in to the page')
def login_to_page(context):
    context.app.login_page.input_email()
    context.app.login_page.input_password()
    context.app.login_page.click_continue_btn()


@when('Click on settings option')
def click_settings_option(context):
    context.app.home_page.click_settings()


@when('Click on Change password option')
def click_change_password_option(context):
    context.app.settings_page.click_change_password()


@then('Verify the right page opens')
def verify_correct_page_opens(context):
    context.app.change_password_page.verify_correct_page_loaded('https://soft.reelly.io/set-new-password')


@then('Add some test password to the input fields')
def input_password(context):
    context.app.change_password_page.enter_new_pw()
    context.app.change_password_page.re_enter_new_pw()


@then('Verify the “Change password” button is available')
def verify_change_password_button_available(context):
    context.app.change_password_page.verify_change_pw_btn_available()
