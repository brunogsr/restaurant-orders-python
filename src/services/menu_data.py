import csv
from src.models.ingredient import Ingredient
from src.models.dish import Dish


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        with open(source_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                name, price, ingredient, amount = row
                dish_instance = Dish(name, float(price))
                if dish_instance not in self.dishes:
                    dish_instance.add_ingredient_dependency(
                        Ingredient(ingredient), int(amount))
                    self.dishes.add(dish_instance)
                else:
                    for dish in self.dishes:
                        if dish == dish_instance:
                            dish.add_ingredient_dependency(
                                Ingredient(ingredient), int(amount))
