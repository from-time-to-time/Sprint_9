import allure
from selenium.webdriver.support import expected_conditions as EC

from src.config import Config
from src.locators.recipes_locators import RecipesPageLocators as R
from src.locators.signin_page_locators import SigninPageLocators as L
from src.pages.base_page import BasePage


class SigninPage(BasePage):
    URL = f"{Config.BASE_URL}signin"

    @property
    def auth_form(self):
        return self.wait_visible(L.AUTH_FORM)

    @allure.step("Открыть страницу авторизации")
    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.visibility_of_element_located(L.EMAIL))
        return self

    @allure.step("Ввести email")
    def fill_email(self, email: str):
        el = self.wait_visible(L.EMAIL)
        el.clear()
        el.send_keys(email)
        return self

    @allure.step("Ввести пароль")
    def fill_password(self, password: str):
        el = self.wait_visible(L.PASSWORD)
        el.clear()
        el.send_keys(password)
        return self

    @allure.step("Нажать «Войти»")
    def click_auth(self):
        from src.pages.recipes_page import RecipesPage
        self.wait_clickable(L.LOGIN_BUTTON).click()
        self.wait.until(EC.visibility_of_element_located(R.TITLE))
        self.wait.until(EC.url_contains(RecipesPage.URL))
        return RecipesPage(self.driver)
