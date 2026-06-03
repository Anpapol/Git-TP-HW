from ingredient import Ingredient

class Recipe:
    def __init__(self, title: str, ingredients: list):
        self.title = title
        self.ingredients = ingredients

    def add_ingredient(self, ingredient: 'Ingredient'):
        for ing in self.ingredients:
            if ing == ingredient:
                ing.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        if type(ratio) in (int, float):
            return ratio > 0
        return False

    def scale(self, ratio: float) -> 'Recipe':
        scaled_ingredients = []
        for ing in self.ingredients:
            new_ing = Ingredient(ing.name, ing.quantity * ratio, ing.unit)
            scaled_ingredients.append(new_ing)
        return Recipe(self.title, scaled_ingredients)

    def __len__(self) -> int:
        return len(self.ingredients)

    def __str__(self) -> str:
        lines = [f"Рецепт: {self.title}"]
        for ing in self.ingredients:
            lines.append(f"- {ing}")
        return "\n".join(lines)
