import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from tests.test_data import TestData  


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def sample_bun():
    return Bun(TestData.BUN_NAME, TestData.BUN_PRICE)


@pytest.fixture
def sample_sauce():
    return Ingredient(TestData.SAUCE_TYPE, TestData.SAUCE_NAME, TestData.SAUCE_PRICE)


@pytest.fixture
def sample_filling():
    return Ingredient(TestData.FILLING_TYPE, TestData.FILLING_NAME, TestData.FILLING_PRICE)


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
    ingredients = []
    
    for ingredient_type, ingredient_name, ingredient_price in TestData.THREE_INGREDIENTS:
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        ingredients.append(ingredient)
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