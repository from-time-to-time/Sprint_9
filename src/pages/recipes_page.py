from src.config import Config
from src.pages.base_page import BasePage


class RecipesPage(BasePage):
    URL = f"{Config.BASE_URL}recipes"
