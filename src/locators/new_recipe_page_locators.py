from selenium.webdriver.common.by import By


class NewRecipePageLocators:
    RECIPE_CARD = (By.XPATH, "(//div[contains(@class, 'style_container')]/div[contains(@class, 'styles_single-card')])")
    RECIPE_TITLE = (By.CSS_SELECTOR, "h1[class*='styles_single-card__title']")
