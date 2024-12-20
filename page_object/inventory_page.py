import allure
from page_object.base_page import BasePage
from data import Data
from locators.inventory_locators import InventoryLocators


class InventoryPage(BasePage):
    @allure.step("открыть страницу Выбора товара")
    def open_inventory_page(self):
        self.open_page(Data.INVENTORY_PAGE)

    @allure.step("открыть страницу Корзины")
    def open_cart_page(self):
        self.open_page(Data.CART_PAGE)

    @allure.step("Добавить Рюкзак в корзину")
    def add_backpack_to_cart(self):
        self.click_element(InventoryLocators.ADD_SAUCE_LABS_BACKPACK)

    @allure.step("Добавить Фонарь в корзину")
    def add_light_to_cart(self):
        self.click_element(InventoryLocators.ADD_SAUCE_LABS_BIKE_LIGHT)

    @allure.step("Добавить Футболку в корзину")
    def add_t_shirt_to_cart(self):
        self.click_element(InventoryLocators.ADD_SAUSE_LABS_BOLT_T_SHIRT)

    @allure.step("Переход в форму информации для оформления заказа по кнопке Checkout")
    def click_to_checkout_button(self):
        self.click_element(InventoryLocators.CHECKOUT_BUTTON)

    @allure.step("Переход в форму оформления заказа по кнопке Continue")
    def click_to_continue_button(self):
        self.click_element(InventoryLocators.CONTINUE_BUTTON)

    @allure.step("Проверка цены Рюкзака")
    def check_sum_backpack(self):
        self.verify_text(InventoryLocators.SUM_FOR_SAUCE_LABS_BACKPACK,"$29.99")

    @allure.step("Проверка цены Фанаря")
    def check_sum_light(self):
        self.verify_text(InventoryLocators.SUM_SAUCE_LABS_BIKE_LIGHT,"$9.99")

    @allure.step("Проверка цены Футболки")
    def check_sum_light(self):
        self.verify_text(InventoryLocators.SUM_FOR_SAUSE_LABS_BOLT_T_SHIRT, "$15.99")

    @allure.step("Проверка элемента в корзине")
    def check_element_in_cart(self, locator: str):
        self.is_element_visible(locator)

