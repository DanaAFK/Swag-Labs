import allure
from page_object.base_page import BasePage
from locators.step_two_locators import StepTwoLocators


class StepTwoPage(BasePage):
    @allure.step("Заполнить форму для оформления заказа")
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str):
        self.type_text(StepTwoLocators.FIRST_NAME, first_name)
        self.type_text(StepTwoLocators.LAST_NAME, last_name)
        self.type_text(StepTwoLocators.ZIP_POSTAL_CODE, postal_code)

    @allure.step("Нажать на кнопку Continue")
    def click_continue_button(self):
        self.click_element(StepTwoLocators.CONTINUE_BUTTON)

    @allure.step("Получить текст суммы заказа")
    def get_total_sum_text(self):
        return self.get_text(StepTwoLocators.TOTAL_SUM)

    @allure.step("Нажать на кнопку Finish")
    def click_finish_button(self):
        self.click_element(StepTwoLocators.FINISH_BUTTON)

    @allure.step("Получить сообщение об успешном оформлении")
    def get_success_message(self):
        return self.get_text(StepTwoLocators.THANK_YOU_MESSAGE)
