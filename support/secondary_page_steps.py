from behave import given, when, then

from time import sleep


###
###

@given('Open Reelly main page')
def open_main(context):
    context.app.main_page.open_main()
    sleep(5)


@given('User is signed into page with email "lubnakh786@gmail.com" and password "123456"')
def open_secondary(context):
    context.app.main_page.click_tab()
    context.app.main_page.click_secondary_tab()



@when('Click on Off-plan tab')
def click_off_plan(context):
    context.app.main_page.click_off_plan_tab()


@when('Click Secondary tab on side menu')
def click_tab(context):
    context.app.main_page.click_tab()
    #context.app.main_page.click_secondary_tab()
    #context.app.secondary_page.verify_secondary_page_opened()


@then('Verify Secondary page opend')
def verify_Secondary_page(context):
    #context.app.Secondary_page.open_()
    context.app.secondary_page.verify_secondary_page_opened()
    # driver.get(context.app.reelly_page.url)
    # driver.get('https://soft.reelly.io/main-menu')
    #context.app.reelly_page.verify_secondary_page_opened()


@when('Clicks on Filters')
def click_filters(context):
    context.app.secondary_page.click_filters()


##

# @then('step Selects the Want to buy option')
# def step_select_want_to_buy(context):
#     context.app.secondary_page.select_want_to_buy()

# @than('slect the want to buy option')
# def select_to_buy(context):
#     context.app.secondary_page.select_to_buy()


@when('click on Apply Filter button')
def click_apply_filter(context):
    context.app.secondary_page.click_apply_filter()


@then('Verify the right page opens')
def verify_secondary_page(context):
    context.app.secondary_page.verify_secondary_page_opened()



#####


# @then("step Selects the Want to buy option")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: Then step Selects the Want to buy optiond')


@when("Clicks on Apply Filter button")
def click_apply_filter(context):
    context.app.secondary_page.click_apply_filter()


@then("Verify all cards have the Want to buy tag")
def verify_want_to_buy_tag(context):
    context.app.secondary_page.verify_want_to_buy_tags()


# # @then("step Selects the Want to buy option")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: Then step Selects the Want to buy option')
@then("step Selects the Want to buy option")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then step Selects the Want to buy option')