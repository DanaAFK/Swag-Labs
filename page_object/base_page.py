import allure
from playwright.sync_api import TimeoutError, Page


class BasePage:

    def __init__(self, driver: Page):
        self.driver = driver

    @allure.step("Открыть определённую страницу")
    def open_page(self, url: str):
        self.driver.goto(url)

    @allure.step("Ожидание элемента с локатором '{locator}' в течение {timeout} мс")
    def wait_for_element(self, locator: str, timeout: int = 10000):
        try:
            self.driver.locator(locator).wait_for(timeout=timeout)
        except TimeoutError:
            allure.attach(
                self.driver.screenshot(),
                name="TimeoutError_Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Таймаут: элемент с локатором {locator} не найден в течение {timeout} мс.")

    @allure.step("Клик по элементу с локатором '{locator}'")
    def click_element(self, locator: str, timeout: int = 10000):

        self.wait_for_element(locator, timeout)
        self.driver.locator(locator).click()

    @allure.step("Ввод текста '{text}' в элемент с локатором '{locator}'")
    def type_text(self, locator: str, text: str, timeout: int = 10000):

        self.wait_for_element(locator, timeout)
        self.driver.locator(locator).fill(text)

    @allure.step("Наведение на элемент с локатором '{locator}'")
    def hover_element(self, locator: str, timeout: int = 10000):

        self.wait_for_element(locator, timeout)
        self.driver.locator(locator).hover()

    @allure.step("Проверка видимости элемента с локатором '{locator}'")
    def is_element_visible(self, locator: str, timeout: int = 10000) -> bool:

        try:
            self.wait_for_element(locator, timeout)
            return self.driver.locator(locator).is_visible()
        except TimeoutError:
            return False

    @allure.step("Получение текста элемента с локатором '{locator}'")
    def get_text(self, locator: str, timeout: int = 10000) -> str:

        self.wait_for_element(locator, timeout)
        return self.driver.locator(locator).inner_text()

    @allure.step("Очистка поля с локатором '{locator}'")
    def clear_field(self, locator: str, timeout: int = 10000):

        self.wait_for_element(locator, timeout)
        self.driver.locator(locator).fill("")

    @allure.step("Проверка наличия текста '{expected_text}' в элементе с локатором '{locator}'")
    def verify_text(self, locator: str, expected_text: str, timeout: int = 10000):

        self.wait_for_element(locator, timeout)
        actual_text = self.get_text(locator, timeout)
        assert actual_text == expected_text, f"Ожидалось '{expected_text}', но найдено '{actual_text}'"

