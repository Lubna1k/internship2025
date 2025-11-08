from pages.base_page import Page
from pages.main_page import MainPage
from pages.offplan_page import OffPlanPage
from pages.verification_page import Verify_Page

# class Application:
#     class Application:
#         def __init__(self, driver):
#             self.driver = driver
#             self.off_plan_page = OffPlanPage(driver)
#             self.secondary_page = SecondaryPage(driver)

def __init__(self,driver):
        self.driver = driver
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.offplan_page=OffPlanPage(driver)
        self.verification_page=Verify_Page(driver)




# from pages.base_page import Page
# from pages.main_page import MainPage
# from pages.secondary_page import SecondaryPage
# from pages.sign_in_page import SignInPage
#
#
# class Application:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#         self.page = Page(driver)
#         self.sign_in_page = SignInPage(driver)
#         self.main_page = MainPage(driver)
#         self.secondary_page = SecondaryPage(driver)

