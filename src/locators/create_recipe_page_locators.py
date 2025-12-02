from selenium.webdriver.common.by import By


class CreateRecipePageLocators:
    TITLE = (By.XPATH, "(//h1[contains(@class, 'styles_title') and contains(text(), 'Создание рецепта')])")
    REC_NAME = (
    By.XPATH, "(//div[contains(text(), 'Название рецепта')]/following-sibling::input[contains(@type, 'text')])")
    BREAKFAST = (By.XPATH, "(//button[contains(@style, 'background-color: orange;')])")
    LUNCH = (By.XPATH, "(//button[contains(@style, 'background-color: green;')])")
    DINNER = (By.XPATH, "(//button[contains(@style, 'background-color: purple;')])")
    ING_NAME = (By.XPATH, "(//div[contains(text(), 'Ингредиенты')]/following-sibling::input[contains(@type, 'text')])")
    ING_LIST = (
    By.XPATH, "(//div[contains(@class,'styles_ingredientsInputs')]//div[contains(@class,'styles_container')])")
    ING = (
    By.XPATH, "(//div[contains(@class,'styles_ingredientsInputs')]//div[contains(@class,'styles_container')])//div[1]")
    WEIGHT = (By.CSS_SELECTOR, "input[class*='styles_ingredientsAmountValue']")
    ADD_ING = (By.CSS_SELECTOR, "div[class*='styles_ingredientAdd']")
    DELETE_BUTTON = (
    By.XPATH, "(//span[contains(@class, 'ingredientsAddedItemRemove') and contains(text(), 'Удалить')])")
    TIME = (
    By.XPATH, "(//div[contains(text(), 'Время приготовления')]/following-sibling::input[contains(@type, 'text')])")
    DESCRIPTION = (By.XPATH, "(//div[contains(text(), 'Описание рецепта')]/following-sibling::textarea)")
    LOAD_PICTURE = (By.XPATH, "(//input[contains(@type, 'file')])")
    CREATE_BUTTON = (By.XPATH, "(//button[contains(@class, 'style_button') and contains(text(), 'Создать рецепт')])")
