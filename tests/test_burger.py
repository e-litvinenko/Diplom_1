import pytest
from unittest.mock import Mock, patch
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from tests.test_data import TestData 


class TestBurger:
    def test_init_bun_is_none(self, burger):
        assert burger.bun is None

    def test_init_ingredients_empty_list(self, burger):
        assert burger.ingredients == []

    def test_set_buns_sets_bun_correctly(self, burger, sample_bun):
        burger.set_buns(sample_bun)
        assert burger.bun == sample_bun

    @pytest.mark.parametrize("ingredient_type,ingredient_name,ingredient_price", 
                             TestData.INGREDIENT_PARAMS)
    def test_add_ingredient_adds_one_ingredient(self, burger, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    @pytest.mark.parametrize("ingredient_count", [2, 5, 10])
    def test_add_ingredient_adds_multiple_ingredients(self, burger, ingredient_count):
        ingredients = [Mock(spec=Ingredient) for _ in range(ingredient_count)]
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)
        assert burger.ingredients == ingredients

    def test_remove_ingredient_removes_by_index(self, burger_with_ingredients):
        burger, sauce, filling = burger_with_ingredients
        burger.remove_ingredient(1)
        assert burger.ingredients == [sauce]
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    @pytest.mark.parametrize("index,new_index,expected_names", 
                             TestData.MOVE_INGREDIENT_CASES)  
    def test_move_ingredient(self, burger_with_three_ingredients, index, new_index, expected_names):
        burger, _ = burger_with_three_ingredients
        burger.move_ingredient(index, new_index)
        actual_names = [ingredient.get_name() for ingredient in burger.ingredients]
        assert actual_names == expected_names

    @pytest.mark.parametrize("bun_price,ingredient_prices,expected", 
                             TestData.PRICE_TEST_CASES)  
    def test_get_price_calculation(self, burger, mock_bun, bun_price, ingredient_prices, expected):
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        for price in ingredient_prices:
            mock_ing = Mock(spec=Ingredient)
            mock_ing.get_price.return_value = price
            burger.add_ingredient(mock_ing)
        assert burger.get_price() == expected

    def test_get_receipt_exact_format_with_real_objects(self):
        burger = Burger()
        burger.set_buns(Bun(TestData.BUN_NAME, TestData.BUN_PRICE))
        burger.add_ingredient(Ingredient(TestData.SAUCE_TYPE, TestData.SAUCE_NAME, TestData.SAUCE_PRICE))
        burger.add_ingredient(Ingredient(TestData.FILLING_TYPE, TestData.FILLING_NAME, TestData.FILLING_PRICE))
        
        with patch.object(burger, 'get_price', return_value=TestData.RECEIPT_TOTAL_PRICE):
            expected = (
                f"(==== {TestData.BUN_NAME} ====)\n"
                f"= sauce {TestData.SAUCE_NAME} =\n"
                f"= filling {TestData.FILLING_NAME} =\n"
                f"(==== {TestData.BUN_NAME} ====)\n\n"
                f"Price: {TestData.RECEIPT_TOTAL_PRICE}"
            )
            
            assert burger.get_receipt() == expected