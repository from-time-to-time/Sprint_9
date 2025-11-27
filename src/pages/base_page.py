import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.config import Config
from src.locators.base_page_locators import BasePageLocators as B


class BasePage:
    def __init__(self, driver, timeout=Config.TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @property
    def logout_button(self):
        return self.wait_visible(B.LOGOUT_BUTTON)

    @allure.step('Открываем главную страницу сайта')
    def open(self, url=None):
        if url is None:
            url = Config.BASE_URL
        self.driver.get(url)
        return self

    @allure.step('Ищем элемент по локатору')
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Ожидаем, пока элемент появится на странице')
    def wait_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step('Ожидаем, пока элемент станет видимым')
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидаем, пока элемент станет невидимым')
    def wait_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step('Ожидаем, пока элемент станет кликабельным')
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step('Нажимаем на элемент')
    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()
        return el

    @allure.step('Скроллим страницу к элементу')
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получаем текущий url страницы')
    def get_current_url(self) -> str:
        return self.driver.current_url

    @allure.step('Ожидаем, что URL будет содержать подстроку')
    def wait_url_contains(self, fragment: str):
        self.wait.until(EC.url_contains(fragment))
        return self

    # ===== Навигация по хедеру =====

    @allure.step('Переходим в «Создать рецепт»')
    def click_create_recipe(self) -> "CreateRecipePage":
        from .create_recipe_page import CreateRecipePage
        self.wait_visible(B.CREATE_RECIPE_BUTTON)
        self.wait_clickable(B.CREATE_RECIPE_BUTTON).click()
        self.wait.until(EC.url_contains(CreateRecipePage.URL))
        return CreateRecipePage(self.driver)

    @allure.step('Переходим в «Создать аккаунт»')
    def click_create_acc(self) -> "SignupPage":
        from .signup_page import SignupPage
        self.wait_visible(B.SIGNUP_BUTTON)
        self.wait_clickable(B.SIGNUP_BUTTON).click()
        self.wait.until(EC.url_contains(SignupPage.URL))
        return SignupPage(self.driver)
