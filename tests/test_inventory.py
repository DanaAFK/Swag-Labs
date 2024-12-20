import allure
from page_object.inventory_page import InventoryPage
from locators.inventory_locators import InventoryLocators
from page_object.login_page import LoginPage


class TestInventory:
    @allure.title("Добавление нескольких товаров в корзину и проверка их суммы")
    def test_add_multiple_items_to_cart(self, driver):

        with allure.step("Авторизоваться под пользователем standard_user"):
            login_page = LoginPage(driver)
            login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        with allure.step("Открыть страницу выбора товара"):
            inventory_page.open_inventory_page()

        with allure.step("Добавить товары в корзину"):
            inventory_page.add_backpack_to_cart()
            inventory_page.add_light_to_cart()
            inventory_page.add_t_shirt_to_cart()

        with allure.step("Проверить, что товары добавлены в корзину"):
            inventory_page.open_cart_page()
            assert inventory_page.is_element_visible(InventoryLocators.SAUCE_LABS_BACKPACK_IN_CART), \
                "Рюкзак не отображается в корзине"
            assert inventory_page.is_element_visible(InventoryLocators.SAUCE_LABS_BIKE_LIGHT_IN_CART), \
                "Фонарь не отображается в корзине"
            assert inventory_page.is_element_visible(InventoryLocators.SAUSE_LABS_BOLT_T_SHIRT_IN_CART), \
                "Футболка не отображается в корзине"

        with allure.step("Проверить цену каждого товара"):
            backpack_price = inventory_page.get_text(InventoryLocators.SUM_FOR_SAUCE_LABS_BACKPACK)
            light_price = inventory_page.get_text(InventoryLocators.SUM_SAUCE_LABS_BIKE_LIGHT)
            t_shirt_price = inventory_page.get_text(InventoryLocators.SUM_FOR_SAUSE_LABS_BOLT_T_SHIRT)

            assert backpack_price == "$29.99", f"Неверная цена рюкзака: ожидалось '$29.99', получено '{backpack_price}'"
            assert light_price == "$9.99", f"Неверная цена фонаря: ожидалось '$9.99', получено '{light_price}'"
            assert t_shirt_price == "$15.99", f"Неверная цена футболки: ожидалось '$15.99', получено '{t_shirt_price}'"

        with allure.step("Проверить общую сумму товаров"):
            total_price = float(backpack_price[1:]) + float(light_price[1:]) + float(t_shirt_price[1:])
            expected_total_price = 29.99 + 9.99 + 15.99
            assert total_price == expected_total_price, \
                f"Неверная общая сумма: ожидалось '{expected_total_price}', получено '{total_price}'"
