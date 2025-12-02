from pathlib import Path

import allure

from src.config import Config
from src.locators.create_recipe_page_locators import CreateRecipePageLocators as C
from src.pages.base_page import BasePage


class CreateRecipePage(BasePage):
    URL = f"{Config.BASE_URL}recipes/create"

    APP_DIR = Path(__file__).resolve().parent.parent
    HELPERS_DIR = APP_DIR / "helpers"

    @allure.step("Ввести название рецепта")
    def fill_recipe_name(self, recipe_name: str):
        el = self.wait_visible(C.REC_NAME)
        el.clear()
        el.send_keys(recipe_name)
        return self

    @allure.step("Нажать «Завтрак»")
    def click_breakfast(self):
        self.wait_clickable(C.BREAKFAST).click()
        return self

    @allure.step("Нажать «Обед»")
    def click_lunch(self):
        self.wait_clickable(C.LUNCH).click()
        return self

    @allure.step("Нажать «Ужин»")
    def click_dinner(self):
        self.wait_clickable(C.DINNER).click()
        return self

    @allure.step("Добавить ингредиент")
    def add_ingredient(self, ing_name: str, weight):
        ing = self.wait_visible(C.ING_NAME)
        ing.clear()
        ing.send_keys(ing_name)
        self.wait_visible(C.ING_LIST)
        self.wait_clickable(C.ING).click()
        self.wait_visible(C.WEIGHT).send_keys(weight)
        self.wait_visible(C.ADD_ING).click()
        return self

    @allure.step("Ввести время приготовления")
    def fill_cooking_time(self, cooking_time: int):
        el = self.wait_visible(C.TIME)
        el.clear()
        el.send_keys(cooking_time)
        return self

    @allure.step("Ввести описание рецепта")
    def fill_description(self, description):
        el = self.wait_visible(C.DESCRIPTION)
        el.clear()
        el.send_keys(description)
        return self

    @allure.step("Добавить фото")
    def add_photo(self, filename):
        file_path = (self.HELPERS_DIR / filename).resolve()
        el = self.wait_presence(C.LOAD_PICTURE)
        el.send_keys(str(file_path))
        return self

    @allure.step("Нажать «Создать рецепт»")
    def click_create_button(self) -> "NewRecipePage":
        from .new_recipe_page import NewRecipePage
        self.wait_clickable(C.CREATE_BUTTON).click()
        return NewRecipePage(self.driver)
