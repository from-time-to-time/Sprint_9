import allure

from src.locators.new_recipe_page_locators import NewRecipePageLocators as N
from src.pages.base_page import BasePage


class NewRecipePage(BasePage):
    @allure.step("Проверяем, что карточка созданного рецепта отображается")
    def is_recipe_card_displayed(self):
        card = self.wait_visible(N.RECIPE_CARD)
        return card.is_displayed()

    @allure.step("Получаем заголовок созданного рецепта")
    def get_recipe_title(self) -> str:
        return self.wait_visible(N.RECIPE_TITLE).text
