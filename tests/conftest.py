import pytest
import allure
from playwright.sync_api import sync_playwright
from data import Data


@allure.title('Фикстура для инициализации и закрытия браузера')
@allure.description(
    'Фикстура инициализирует выбранный браузер (Firefox или Chrome) для каждого теста'
)
@pytest.fixture(scope="function", params=["chromium", "firefox"])
def driver(request):
    browser = None
    context = None
    page = None

    try:
        with sync_playwright() as p:
            if request.param == "chromium":
                browser = p.chromium.launch(headless=False)
            elif request.param == "firefox":
                browser = p.firefox.launch(headless=False)
            else:
                pytest.fail(f"Unsupported browser type: {request.param}")

            # Создание контекста браузера и страницы
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            page = context.new_page()

            # Установка начальной страницы
            page.goto(Data.URL)

            yield page  # Передаем страницу тестам

    except Exception as e:
        pytest.fail(f"Ошибка при инициализации браузера: {e}")
    finally:
        if page:
            page.close()
        if context:
            context.close()
        if browser:
            browser.close()
