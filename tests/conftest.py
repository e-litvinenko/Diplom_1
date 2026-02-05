# tests/unit/conftest.py
import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def sample_bun():
    return Bun("Тестовая булочка", 100.0)


@pytest.fixture
def sample_sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "Тестовый соус", 50.0)


@pytest.fixture
def sample_filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, "Тестовая начинка", 150.0)


@pytest.fixture
def burger_with_bun(burger, sample_bun):
    burger.set_buns(sample_bun)
    return burger


@pytest.fixture
def burger_with_ingredients(burger_with_bun, sample_sauce, sample_filling):
    burger = burger_with_bun
    burger.add_ingredient(sample_sauce)
    burger.add_ingredient(sample_filling)
    return burger, sample_sauce, sample_filling


@pytest.fixture
def burger_with_three_ingredients(burger_with_bun):
    burger = burger_with_bun
    ingredients = [
        Ingredient(INGREDIENT_TYPE_SAUCE, "Соус 0", 10.0),
        Ingredient(INGREDIENT_TYPE_FILLING, "Мясо 1", 20.0),
        Ingredient(INGREDIENT_TYPE_SAUCE, "Соус 2", 30.0)
    ]
    
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)
    
    return burger, ingredients


@pytest.fixture
def mock_bun():
    mock = Mock(spec=Bun)
    mock.get_price.return_value = 100.0
    mock.get_name.return_value = "Мок булочка"
    return mock


@pytest.fixture
def mock_ingredient():
    mock = Mock(spec=Ingredient)
    mock.get_price.return_value = 50.0
    mock.get_name.return_value = "Мок ингредиент"
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock