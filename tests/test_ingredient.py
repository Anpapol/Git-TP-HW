from main import Ingredient

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
