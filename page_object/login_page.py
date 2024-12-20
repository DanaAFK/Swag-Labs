import allure
from page_object.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):

    @allure.step("Ввод имени пользователя: {username}")
    @allure.description(
        ':param username: Имя пользователя.'
    )
    def enter_username(self, username: str):

        self.type_text(LoginLocators.USERNAME_INPUT, username)

    @allure.step("Ввод пароля")
    @allure.description(
        ':param password: Пароль пользователя.'
    )
    def enter_password(self, password: str):

        self.type_text(LoginLocators.PASSWORD_INPUT, password)

    @allure.step("Клик на кнопку входа")
    def click_login_button(self):

        self.click_element(LoginLocators.LOGIN_BUTTON)

    @allure.step("Проверка успешного входа")
    @allure.description(
        ':return: True, если контейнер инвентаря отображается, иначе False.'
    )
    def is_inventory_page_displayed(self):

        return self.is_element_visible(LoginLocators.INVENTORY_CONTAINER)

    @allure.step("Проверка появления окна об ошибке")
    @allure.description(
        ':return: True, если сообщение появилось, иначе False.'
    )
    def is_error_message(self):

        return self.is_element_visible(LoginLocators.ERROR_MESSAGE)

    @allure.step("Проверка текста сообщения об ошибке")
    @allure.description(
        'получает текст локатора ERROR_MESSAGE'
    )
    def get_error_text(self):

        return self.get_text(LoginLocators.ERROR_MESSAGE)

    @allure.step("Вход в учетную запись с именем {username}")
    @allure.description(
        ':param username: Имя пользователя.'
        ':param password: Пароль пользователя.'
    )
    def login(self, username: str, password: str):

        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()