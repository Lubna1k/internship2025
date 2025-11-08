from selenium import webdriver
from selenium.webdriver.chrome.service import Service



from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application


def browser_init(context,scenario_name):
    """
    :param context: Behave context
    """

    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)



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

    #stopcode
    # setx_BROWSERSTACK_USERNAME =  "lubnakhan_YAZ93C"
    # setx_BROWSERSTACK_ACCESS_KEY = "GoDEKiq3Zsz5UZcEacz"
    #
    # setBROWSERSTACK_USERNAME = "lubnakhan_YAZ93C"
    # setBROWSERSTACK_ACCESS_KEY = "GoDEKiq3Zsz5UZcEacz"


    # Browser Stack
    bs_user = 'lubnakhanlk_yAZ93C'
    bs_key = 'GoDEkiq3Zsz5UzZcEacz'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    ###browserstack Mobile###



    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    # BrowserStack Mobile Testing
    bstack_options = {
        "deviceName": "Samsung Galaxy S20 Ultra",
        "osVersion": "10.0",
        "realMobile": "true",
        "browserName": "chrome",
        "sessionName": scenario_name,
        "buildName": "Mobile Web Run",
        "projectName": "Mobile Web Tests"
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    # MobileEmulationTesting
    # mobile_emulation = { "deviceName": "iPhone 12 Pro" }
    #
    # chrome_options = Options()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # chrome_options.add_argument("--start-maximized")
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service, options=chrome_options)

    context.driver.implicitly_wait(5)
    # context.driver.get("https://www.google.com")

    # NormelMode
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    context.app = Application(context.driver)

    # Debug info to confirm emulation
    # user_agent = context.driver.execute_script("return navigator.userAgent;")
    # print("User Agent:", user_agent)
    # viewport = context.driver.execute_script("return [window.innerWidth, window.innerHeight];")
    # print("Viewport size:", viewport)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()

    # options = Options()
    # # #Browser  tack web
    # # bstack_options = {
    # #     "osVersion": "13.0",
    # #     "deviceName": "Samsung Galaxy S20 Ultra",
    # #     "realMobile": "true",
    # #     "browserName": "Chrome",
    # #     "projectName": "Reelly Tests",
    # #     "buildName": "Mobile Android Run",
    # #     "sessionName": scenario_name
    # # }
    # #
############

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

 #context.driver.maximize_window()


