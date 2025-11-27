from selenium.webdriver.common.by import By


class SignupPageLocators:
    TITLE = (By.XPATH, "(//h1[contains(@class, 'styles_title') and contains(text(), 'Регистрация')])")
    NAME = (By.XPATH, "(//input[@name = 'first_name'])")
    LASTNAME = (By.XPATH, "(//input[@name = 'last_name'])")
    USERNAME = (By.XPATH, "(//input[@name = 'username'])")
    EMAIL = (By.XPATH, "(//input[@name = 'email'])")
    PASSWORD = (By.XPATH, "(//input[@name = 'password'])")
    SIGNUP_BUTTON = (By.XPATH, "(//button[contains(@class, 'style_button') and contains(text(), 'Создать аккаунт')])")
