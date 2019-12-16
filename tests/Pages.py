from tests.BaseApp import BasePage
from selenium.webdriver.common.by import By


class SearchLocators:
    LOCATOR_MENU_BUTTON = (By.CLASS_NAME, "nav.nav button.humb")
    LOCATOR_MENU_CLICK_ON_CLEANMYMAC_X = (By.XPATH, '//a[@data-qa="cleanmymac-x-in-menu"]')
    LOCATOR_MENU_CLEANMYMAC_X_CLICK_DAWNLOAD = (By.XPATH, '//a[@data-qa="FreeDownloadBtn"]')
    LOCATOR_CLEANMYMAC_X_POP_UP_ENTER_MAIL = (By.CSS_SELECTOR, '#overlay .modal input[type=\"email\"]')
    LOCATOR_CLEANMYMAC_X_POP_UP_SUBSCRIBE = (By.CSS_SELECTOR, ".subscribe:nth-child(2) .btn")
    LETS_GET_SOCIAL_WERE_ALWAYS_ON = (By.CSS_SELECTOR, 'p:nth-child(3)')


class SearchHelper(BasePage):
    def click_on_menu_button(self):
        return self.find_element(SearchLocators.LOCATOR_MENU_BUTTON, 4).click()

    def menu_click_on_cleanmymac_x(self):
        return self.find_element(SearchLocators.LOCATOR_MENU_CLICK_ON_CLEANMYMAC_X, 4).click()

    def cleanmymac_x_click_dawnload(self):
        return self.find_element(SearchLocators.LOCATOR_MENU_CLEANMYMAC_X_CLICK_DAWNLOAD, 4).click()

    def cleanmymac_x_pop_up_enter_mail(self, mail):
        search_field = self.find_element(SearchLocators.LOCATOR_CLEANMYMAC_X_POP_UP_ENTER_MAIL, 4)
        search_field.click()
        search_field.send_keys(mail)
        return search_field

    def cleanmymac_x_pop_up_subscribe(self):
        return self.find_element(SearchLocators.LOCATOR_CLEANMYMAC_X_POP_UP_SUBSCRIBE).click()

    def confirm_subscription(self, ur):
        return self.go_to_site(sec_url=ur)

    def lets_get_social_were_always_on(self):
        return self.find_element(SearchLocators.LETS_GET_SOCIAL_WERE_ALWAYS_ON).text

