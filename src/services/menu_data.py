import csv
from src.models.ingredient import Ingredient
from src.models.dish import Dish


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = []

        with open(source_path, "r") as file:
            file_reader = csv.reader(file, delimiter=",")
            header, *data = file_reader

            for name, price, ingredient, recipe_amount in data:
                price = float(price)
                recipe_amount = int(recipe_amount)

                # Verifica se o prato já existe na lista, se não, cria um novo
                dish = next((d for d in self.dishes if d.name == name), None)
                if dish is None:
                    dish = Dish(name, price)
                    self.dishes.append(dish)

                # Adiciona o ingrediente ao prato
                new_ingr = Ingredient(ingredient)
                dish.add_ingredient_dependency(new_ingr, recipe_amount)
