# tests/unit/test_data.py
"""Модуль с тестовыми данными для тестов Burger"""

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestData:
    """Класс с тестовыми данными для тестов Burger"""
    
    # Данные для фикстуры sample_bun
    BUN_NAME = "Тестовая булочка"
    BUN_PRICE = 100.0
    
    # Данные для фикстуры sample_sauce
    SAUCE_TYPE = INGREDIENT_TYPE_SAUCE
    SAUCE_NAME = "Тестовый соус"
    SAUCE_PRICE = 50.0
    
    # Данные для фикстуры sample_filling
    FILLING_TYPE = INGREDIENT_TYPE_FILLING
    FILLING_NAME = "Тестовая начинка"
    FILLING_PRICE = 150.0
    
    # Данные для фикстуры burger_with_three_ingredients
    THREE_INGREDIENTS = [
        (INGREDIENT_TYPE_SAUCE, "Соус 0", 10.0),
        (INGREDIENT_TYPE_FILLING, "Мясо 1", 20.0),
        (INGREDIENT_TYPE_SAUCE, "Соус 2", 30.0)
    ]
    
    # Данные для параметризованного теста test_add_ingredient_adds_one_ingredient
    INGREDIENT_PARAMS = [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
        (INGREDIENT_TYPE_FILLING, "beef", 150.0),
    ]
    
    # Данные для параметризованного теста test_move_ingredient
    MOVE_INGREDIENT_CASES = [
        (2, 0, ["Соус 2", "Соус 0", "Мясо 1"]),
        (0, 2, ["Мясо 1", "Соус 2", "Соус 0"]),
        (1, 1, ["Соус 0", "Мясо 1", "Соус 2"]),
    ]
    
    # Данные для параметризованного теста test_get_price_calculation
    PRICE_TEST_CASES = [
        (100.0, [], 200.0),
        (100.0, [50.0], 250.0),
        (100.0, [50.0, 70.0, 30.0], 350.0),
    ]
    
    # Данные для теста квитанции (используем уже существующие данные)
    RECEIPT_TOTAL_PRICE = 430.0