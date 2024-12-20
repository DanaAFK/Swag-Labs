import allure
from page_object.login_page import LoginPage
from page_object.inventory_page import InventoryPage
from page_object.step_two_page import StepTwoPage


class TestStepTwo:
    @allure.title("Авторизация с валидными данными")
    def test_order_completion(self, driver):
        with allure.step("Шаг 1: Авторизоваться под пользователем standard_user"):
            login_page = LoginPage(driver)
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Шаг 2: Добавить три товара в корзину"):
            inventory_page = InventoryPage(driver)
            inventory_page.add_backpack_to_cart()
            inventory_page.add_light_to_cart()
            inventory_page.add_t_shirt_to_cart()

        with allure.step("Шаг 3: Перейти на страницу корзины"):
            inventory_page.open_cart_page()

        with allure.step("Шаг 4: Нажать на кнопку Checkout"):
            inventory_page.click_to_checkout_button()

        with allure.step("Шаг 5: Заполнить данные формы"):
            step_two_page = StepTwoPage(driver)
            step_two_page.fill_checkout_form("Dana", "Ivanova", "123456")

        with allure.step("Шаг 6: Нажать на кнопку Continue"):
            step_two_page.click_continue_button()

        with allure.step("Шаг 7: Проверить сумму заказа"):
            total_sum_text = step_two_page.get_total_sum_text()
            assert total_sum_text == "Total: $60.45", \
                f"Неверная сумма заказа: ожидалось 'Total: $60.45', получено '{total_sum_text}'"

        with allure.step("Шаг 8: Нажать на кнопку Finish"):
            step_two_page.click_finish_button()

        with allure.step("Шаг 9: Проверить сообщение об успешном оформлении"):
            success_message = step_two_page.get_success_message()
            assert success_message == ('Thank you for your order!\n'
                                       'Your order has been dispatched, and will arrive just as fast as the pony can '
                                       'get there!\n'
                                       'Back Home'), \
                f"Сообщение об успешном оформлении неверное: ожидалось 'Thank you for your order!', " \
                f"получено '{success_message}'"