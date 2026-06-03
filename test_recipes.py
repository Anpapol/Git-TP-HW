import pytest

from main import Ingredient
from main import Recipe

def test_ingredient_creation():
    ing = Ingredient("Мука", 500.0, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit == "г"

def test_ingredient_str():
    ing = Ingredient("Мука", 500.0, "г")
    assert str(ing) == "Мука: 500.0 г"

def test_ingredient_eq_same_name_and_unit():
    ing1 = Ingredient("Мука", 500.0, "г")
    ing2 = Ingredient("Мука", 300.0, "г")
    assert ing1 == ing2

def test_ingredient_eq_different_name():
    ing1 = Ingredient("Мука", 500.0, "г")
    ing2 = Ingredient("Сахар", 500.0, "г")
    assert ing1 != ing2

def test_ingredient_eq_different_unit():
    ing1 = Ingredient("Мука", 500.0, "г")
    ing2 = Ingredient("Мука", 500.0, "кг")
    assert ing1 != ing2

def test_recipe_creation():
    ingredients_list = []
    recipe = Recipe("Блины", ingredients_list)
    assert recipe.title == "Блины"
    assert recipe.ingredients == ingredients_list

def test_add_new_ingredient():
    recipe = Recipe("Блины", [])
    ing = Ingredient("Мука", 500, "г")
    recipe.add_ingredient(ing)
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0] == ing

def test_add_duplicate_ingredient_sums_quantity():
    recipe = Recipe("Блины", [])
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    recipe.add_ingredient(Ingredient("Мука", 200, "г"))
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].quantity == 700.0

def test_scale_returns_new_object_with_multiplied_quantity():
    ing1 = Ingredient("Мука", 500, "г")
    ing2 = Ingredient("Яйца", 2, "шт")
    recipe = Recipe("Блины", [ing1, ing2])
    
    scaled_recipe = recipe.scale(2)
    
    assert scaled_recipe is not recipe
    assert scaled_recipe.title == "Блины"
    assert scaled_recipe.ingredients[0].quantity == 1000.0
    assert scaled_recipe.ingredients[1].quantity == 4.0
    assert recipe.ingredients[0].quantity == 500.0
    assert recipe.ingredients[1].quantity == 2.0

def test_scale_invalid_ratio_raises_error():
    ing = Ingredient("Мука", 500, "г")
    recipe = Recipe("Блины", [ing])
    
    with pytest.raises(ValueError):
        recipe.scale(0)
        
    with pytest.raises(ValueError):
        recipe.scale(-1.5)

def test_recipe_len_returns_unique_ingredients_count():
    recipe = Recipe("Блины", [])
    assert len(recipe) == 0

    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    recipe.add_ingredient(Ingredient("Молоко", 1, "л"))
    assert len(recipe) == 2

    recipe.add_ingredient(Ingredient("Мука", 100, "г"))
    assert len(recipe) == 2




    
