from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from app.application import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """


    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # ## HEADLESS MODE Chrome ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument("window-size=1920x1080")
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    # ## Firefox ###
    # service = Service(executable_path='/Users/yanaamericana/Desktop/Internship-project-automation/geckodriver')
    # context.driver = webdriver.Firefox(service=service)

    ## BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = '*****'
    bs_key = '*****'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        'os': 'Windows',
        'osVersion': '10',
        'browserName': 'Firefox',
        'sessionName': scenario_name
    }

    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.wait = WebDriverWait(context.driver, 15)
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
