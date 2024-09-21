from datetime import timedelta
import pytest
from Src.Models.recipe import recipe_model
from Src.Models.ingredients import Ingredient
from Src.Models.range import range_model
from Src.Models.nomenclature import nomenclature_model
from Src.Models.group import group_model
from Src.Core.validator import argument_exception


def test_recipe_item_validation():
    # Проверка на неправильные типы для ингредиентов
    with pytest.raises(argument_exception):
        Ingredient('', range_model(1, "граммы"))  # Неправильный тип для номенклатуры

    with pytest.raises(argument_exception):
        Ingredient(nomenclature_model(name='Мука', group=group_model(), range=None), '')  # Неправильный тип для количества

def test_recipe_validation():
    # Корректная инициализация рецепта
    recipe_model(
        name='Тестовый рецепт',
        cooking_time=timedelta(minutes=10),
        ingredients=[],
        cooking_steps=[]
    )

    # Проверка на неправильные типы для параметров рецепта
    with pytest.raises(argument_exception):
        recipe_model(name=1, cooking_time=timedelta(minutes=10), ingredients=[], cooking_steps=[])

    with pytest.raises(argument_exception):
        recipe_model(name='Тест', cooking_time=timedelta(minutes=10), ingredients={}, cooking_steps=[])

    with pytest.raises(argument_exception):
        recipe_model(name='Тест', cooking_time=1, ingredients=[], cooking_steps=[])

    with pytest.raises(argument_exception):
        recipe_model(name='Тест', cooking_time=timedelta(minutes=10), ingredients=[], cooking_steps=1)
