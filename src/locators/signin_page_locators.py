from selenium.webdriver.common.by import By


class SigninPageLocators:
    TITLE = (By.XPATH, "(//h1[contains(@class, 'styles_title') and contains(text(), 'Войти на сайт')])")
    AUTH_FORM = (By.XPATH, "//form[contains(@class, 'styles_form')]")
    EMAIL = (By.XPATH, "(//input[@name = 'email'])")
    PASSWORD = (By.XPATH, "(//input[@name = 'password'])")
    LOGIN_BUTTON = (By.XPATH, "(//button[contains(@class, 'style_button') and contains(text(), 'Войти')])")
