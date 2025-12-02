import allure

from src.helpers.data import UserData as U
from src.pages.recipes_page import RecipesPage
from src.pages.signin_page import SigninPage


class TestSignIn:
    @allure.title('Проверка авторизации')
    def test_signin(self, driver):
        signin_page = SigninPage(driver).open()
        signin_page.fill_email(U.USERNAME)
        signin_page.fill_password(U.PASSWORD)
        recipes_page = signin_page.click_auth()

        assert recipes_page.get_current_url() == RecipesPage.URL, f'Ожидали {RecipesPage.URL}, получили {recipes_page.get_current_url()}'
        assert recipes_page.logout_button.is_displayed(), 'Кнопка "Выход" не отображается'
