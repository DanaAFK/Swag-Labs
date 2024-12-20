import pytest
import allure
from page_object.login_page import LoginPage
from locators.login_locators import LoginLocators
from data import Data


class TestLogin:

    @allure.title('Тест на успешный вход в учетную запись с разными именами пользователя.')
    @pytest.mark.parametrize("username", [
        "standard_user",
        "locked_out_user",
        "problem_user",
        "performance_glitch_user",
        "error_user",
        "visual_user",
    ])
    def test_successful_login(self, driver, username):
        login_page = LoginPage(driver)

        # Вход с валидными учетными данными
        login_page.login(username, Data.PASSWORD)

        # Проверяем, что страница инвентаря отображается
        assert login_page.is_inventory_page_displayed(), f"Пользователь {username} не смог войти"

    @allure.title('Тест проверяет, что сообщение об ошибке появляется'
                  'при вводе неверных данных в поля Username и Password.')
    @pytest.mark.parametrize("username, password", [
        (LoginLocators.INVALID_USERNAME, LoginLocators.INVALID_PASSWORD)
    ])
    def test_error_message_invalid_login(self, driver, username, password):
        # Открытие страницы
        login_page = LoginPage(driver)
        login_page.login(username, password)

        assert login_page.is_error_message()

        # Проверка текста сообщения об ошибке
        assert login_page.get_error_text() == LoginLocators.ERROR_MESSAGE_TEXT, f"Неверный текст ошибки"