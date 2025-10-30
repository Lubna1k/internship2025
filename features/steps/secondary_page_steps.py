from selenium.webdriver.common.by import By
from behave import given, when, then


from pages.main_page import MainPage



# @given('Open Reelly secondary page')
# def open_secondary(context):
#     context.app.main_page.click_tab()
#     context.app.main_page.click_secondary_tab()




@when('Clicks on Filters')
def click_filters(context):
    context.app.secondary_page.click_filters()



@when('Selects the Want to buy option')
def select_want_to_buy(context):
    context.app.secondary_page.select_want_to_buy()



@when('Clicks on Apply Filter button')
def click_apply_filter(context):
    context.app.secondary_page.click_apply_filter()



@then('Verify all cards have the Want to buy tag')
def verify_want_to_buy_tags(context):
    context.app.secondary_page.verify_want_to_buy_tags()


@then('Verify the right page opens')
def verify_secondary_page(context):
    context.app.secondary_page.verify_secondary_page_opened()



# import webdriver_manager
# from selenium.webdriver.common.by import By
# from behave import given, when, then
#
#
#
# SEARCH_INPUT = (By.NAME, 'q')
# SEARCH_SUBMIT = (By.NAME, 'btnK')
#
# # webdriver_manager..chrome.ChromeDriverManager().install()
#
#
# @given('open reelly main page')
# def relly(context):
#     context.driver.get('https://soft.reelly.io/main-menu')
#
#
# @given('Open Reelly secondary page')
# def open_secondary(context):
#     context.app.main_page.click_tab()
#     context.app.main_page.click_secondary_tab()
#
#
#
# @given('User is signed into page with email "lubnakh786@gmail.com" and password "123456"')
# def open_secondary(context):
#     context.app.main_page.click_tab()
#     context.app.main_page.click_secondary_tab()
#
#
# @when('Click on the Secondary tab on side menu')
# def click_tab(context):
#     context.app.main_page.click_tab()
#     context.app.main_page.click_secondary_tab()
#     context.app.secondary_page.verify_secondary_page_opened()
#
#
# @then('Verify the right page opens')
# def verify_secondary_page(context):
#     context.app.secondary_page.verify_secondary_page_opened()
#     context.app.secondary_page.verify_secondary_page_title()
#
#
#
#
#
# @when('Clicks on Filters')
# def click_filters(context):
#     context.app.secondary_page.click_filters()
#
# @when('Selects the Want to buy option')
# def select_want_to_buy(context):
#     context.app.secondary_page.select_want_to_buy()
#
# @when('Clicks on Apply Filter button')
# def click_apply_filter(context):
#     context.app.secondary_page.click_apply_filter()
#
# @then('Verify all cards have the Want to buy tag')
# def verify_want_to_buy_tags(context):
#     context.app.secondary_page.verify_want_to_buy_tags()
#
# @then('Verify the right page opens')
# def verify_secondary_page(context):
#     context.app.secondary_page.verify_secondary_page_opened()