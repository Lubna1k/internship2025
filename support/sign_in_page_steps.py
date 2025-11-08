from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('I open the Reelly sign-up page')
def open_google(context):
    context.driver.get('https://soft.reelly.io/sign-up')
    context.app.sign_up_page.open_sign_up()
    sleep()





@when('Reelly search field is filled with')
def input_search(context):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys("Sign_page")
    sleep(4)




@given('User is signed into page with email "lubnakh786@gmail.com" and password 123456')
def sign_in(context):
    context.driver.find_element(By.NAME, 'email').send_keys("lubnakh786@gmail.com")
    context.driver.find_element(By.NAME, 'password').send_keys("123456")
    context.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    sleep(5)


@when('Reelly search field is filled with')
def input_search(context):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys("Sign_page")
    sleep(4)


# from selenium.webdriver.common.by import By
# from behave import given, when, then
#
#
# @given('User is signed into page with email "{email}" and password "{password}"')
# def sign_into_page(context, email, password):
#     context.app.sign_in_page.sign_in(email, password)

