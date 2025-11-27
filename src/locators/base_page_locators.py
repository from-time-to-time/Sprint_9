from selenium.webdriver.common.by import By


class BasePageLocators:
    RECIPES_ICON = (By.CSS_SELECTOR, 'a[href="/recipes"]')
    SIGNIN_BUTTON = (By.CSS_SELECTOR, 'a[href="/signin"][class*="styles_menu"]')
    SIGNUP_BUTTON = (By.CSS_SELECTOR, 'a[href="/signup"]')
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(@class, 'styles_menu') and contains(text(), 'Выход')]")
    CREATE_RECIPE_BUTTON = (By.CSS_SELECTOR, 'a[href="/recipes/create"]')
