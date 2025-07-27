from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.firefox import GeckoDriverManager
# from app.application import Application
#class Page:

def __init__(self, driver):
    self.driver = driver
    self.base_url = 'https://soft.reelly.io'
    self.wait = WebDriverWait(self.driver, timeout=10)



def open_url(self, url):
 self.driver.get(url)

def find_element(self, *locator):
    return self.driver.find_element(*locator)


def find_elements(self, *locator):
    return self.driver.find_elements(*locator)

def click(self, *locator):
    self.driver.find_element(*locator).click()

def input_text(self, text, *locator):
    self.driver.find_element(*locator).send_keys(text)

def wait_until_clickable(self, *locator):
   self.wait.until(EC.element_to_be_clickable(locator),
   message=f'Element not clickable by {locator}'
 )

def wait_until_clickable_click(self, *locator):
    self.wait.until(EC.element_to_be_clickable(locator),
    message=f'Element not clickable by {locator}'
  ).click()

def wait_until_visible(self, *locator):
    self.wait.until(EC.visibility_of_element_located(locator),
    message=f'Element not visible by {locator}'
  )

def wait_until_invisible(self, *locator):
    self.wait.until(EC.invisibility_of_element_located(locator),
   message=f'Element still visible by {locator}'
 )

def verify_url(self, expected_url):
    current_url = self.driver.current_url
    print(f'Current url {current_url}')
    assert expected_url == current_url, f'Expected URL {expected_url}, but got {current_url}'