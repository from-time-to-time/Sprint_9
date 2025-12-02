import allure

from src.pages.base_page import BasePage
from src.pages.signin_page import SigninPage
from src.pages.signup_page import SignupPage


class TestSignUp:
    @allure.title('Проверка создания аккаунта')
    def test_registration(self, driver, name, lastname, username, email, password):
        home = BasePage(driver).open()
        page = home.click_create_acc()
        page.wait_url_contains(SignupPage.URL)
        page.fill_name(name)
        page.fill_lastname(lastname)
        page.fill_username(username)
        page.fill_email(email)
        page.fill_password(password)
        signin = page.create_acc()

        assert signin.get_current_url() == SigninPage.URL, f'Ожидали {SigninPage.URL}, получили {signin.get_current_url()}'
        assert signin.auth_form.is_displayed(), 'Форма авторизации не отображается'
