class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: list):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio: float) -> 'DietaryRecipe':
        recipe = super().scale(ratio)
        return DietaryRecipe(recipe.title, self.diet_type, recipe.ingredients)

    def __str__(self) -> str:
        recipe = super().__str__()
        return recipe.replace("Рецепт:", f"[{self.diet_type}]", 1)
