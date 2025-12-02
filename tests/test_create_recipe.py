import allure

from src.helpers.data import RecipeData as R


class TestCreateRecipe:
    @allure.title('Проверка создания рецепта')
    def test_create_recipe(self, authorize):
        recipes_page = authorize
        page = recipes_page.click_create_recipe()
        recipe_name = R.TITLE
        page.fill_recipe_name(recipe_name)
        page.click_lunch()
        page.click_dinner()
        page.add_ingredient(R.ING_1, R.WEIGHT_1)
        page.add_ingredient(R.ING_2, R.WEIGHT_2)
        page.add_ingredient(R.ING_3, R.WEIGHT_3)
        page.add_ingredient(R.ING_4, R.WEIGHT_4)
        page.fill_cooking_time(R.TIME)
        page.fill_description(R.DESCRIPTION)
        page.add_photo("blinchiki.png")
        new_recipe_page = page.click_create_button()

        assert new_recipe_page.is_recipe_card_displayed()
        assert new_recipe_page.get_recipe_title() == recipe_name
