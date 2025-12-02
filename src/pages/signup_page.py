import allure
from selenium.webdriver.support import expected_conditions as EC

from src.config import Config
from src.locators.signin_page_locators import SigninPageLocators as L
from src.locators.signup_page_locators import SignupPageLocators as S
from src.pages.base_page import BasePage


class SignupPage(BasePage):
    URL = f"{Config.BASE_URL}signup"

    @allure.step("Открыть страницу регистрации")
    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.visibility_of_element_located(S.TITLE))
        return self

    @allure.step("Ввести имя")
    def fill_name(self, name: str):
        el = self.wait_visible(S.NAME)
        el.clear()
        el.send_keys(name)
        return self

    @allure.step("Ввести фамилию")
    def fill_lastname(self, lastname: str):
        el = self.wait_visible(S.LASTNAME)
        el.clear()
        el.send_keys(lastname)
        return self

    @allure.step("Ввести юзернейм")
    def fill_username(self, username: str):
        el = self.wait_visible(S.USERNAME)
        el.clear()
        el.send_keys(username)
        return self

    @allure.step("Ввести email")
    def fill_email(self, email: str):
        el = self.wait_visible(S.EMAIL)
        el.clear()
        el.send_keys(email)
        return self

    @allure.step("Ввести пароль")
    def fill_password(self, password: str):
        el = self.wait_visible(S.PASSWORD)
        el.clear()
        el.send_keys(password)
        return self

    @allure.step("Нажать «Создать аккаунт»")
    def create_acc(self):
        from src.pages.signin_page import SigninPage
        self.wait_clickable(S.SIGNUP_BUTTON).click()
        self.wait.until(EC.visibility_of_element_located(L.TITLE))
        self.wait.until(EC.url_contains(SigninPage.URL))
        return SigninPage(self.driver)
