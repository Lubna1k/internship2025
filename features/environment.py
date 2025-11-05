from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.chrome.options import Options

from app.application import Application

#####from allure_behave.utils import scenario_name



def browser_init(context):

#def browser_init(context, scenario_name):
# browserstack######
    """
    :param context: Behave context
    """


    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)


 #   context.driver = webdriver.Chrome()
###### other Browser in #######
    #Chrome Browser
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # Firefox Browser
    #context.driver = webdriver.Firefox()


    # Headless Mode####-
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver =  webdriver.Chrome(
    #     options=options
    # )
######### my broeserstack###########

    # setx_BROWSERSTACK_USERNAME =  "lubnakhan_YAZ93C"
    # setx_BROWSERSTACK_ACCESS_KEY = "GoDEKiq3Zsz5UZcEacz"
    #
    # setBROWSERSTACK_USERNAME = "lubnakhan_YAZ93C"
    # setBROWSERSTACK_ACCESS_KEY = "GoDEKiq3Zsz5UZcEacz"


    # Browser Stack
    # bs_user = 'lubnakhanlk_yAZ93C'
    # bs_key = 'GoDEkiq3Zsz5UzZcEacz'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os": "win",
    #     "browserName": "chrome",
    #     "browserVersion": "latest",
    #     'browserName': 'Firefox',
    #     'sessionName': scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)
   # browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()


    #cloud testing browserstack##########