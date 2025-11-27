from selenium.webdriver.common.by import By


class RecipesPageLocators:
    TITLE = (By.XPATH, "(//h1[contains(@class, 'styles_title') and contains(text(), 'Рецепты')])")
