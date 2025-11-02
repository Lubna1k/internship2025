from selenium.webdriver.common.by import By
from behave import given, when, then


from pages.main_page import MainPage
from behave import given, when, then
#import os

@given('open reelly site page')
def relly(context):
    context.driver.get('https://soft.reelly.io/main-menu')
    context.driver.implicitly_wait(5)

# @given("Open Reelly site page")
# def open_site_page(context):
#     context.app.login_page.open_login()



@given("Log in to Reelly account")
def login(context):
    context.app.login_page.complete_login("Lubnakh786@gmail.com", "123456")



@when('Click on "Off-plan" in left side menu')
def click_off_plan(context):
    context.app.sidebar_page.open_off_plan()



@then("Verify Off-plan page is opened")
def verify_off_plan_page(context):
    context.app.off_plan_page.verify_off_plan_page_opened()



@when('Filter by sale status "Announced"')
def filter_announced(context):
    context.app.off_plan_page.filter_by_announced()



@then('Verify all projects have status "Announced"')
def verify_announced(context):
    context.app.off_plan_page.verify_announced_results()