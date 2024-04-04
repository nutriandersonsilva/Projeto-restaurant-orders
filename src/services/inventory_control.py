from csv import DictReader
from typing import Dict

from src.models.dish import Recipe
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path: str = BASE_INVENTORY) -> Inventory:
    """Lê os dados do inventário de um arquivo CSV e retorna um dicionário."""
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


class InventoryMapping:
    def __init__(self, inventory_file_path: str = BASE_INVENTORY) -> None:
        """Inicializa o InventoryMapping com dados de um arquivo CSV."""
        self.inventory = read_csv_inventory(inventory_file_path)

    def check_recipe_availability(self, recipe: Recipe) -> bool:
        """Verifica se há ingredientes suficientes no inventário para uma receita."""
        for ingredient, amount in recipe.items():
            if (
                ingredient not in self.inventory
                or self.inventory[ingredient] < amount
            ):
                return False
        return True

    def consume_recipe(self, recipe: Recipe) -> None:
        """Consome ingredientes do inventário com base em uma receita."""
        if not self.check_recipe_availability(recipe):
            raise ValueError("Não há ingredientes suficientes no inventário")

        for ingredient, amount in recipe.items():
            self.inventory[ingredient] -= amount

        if any(amount < 0 for amount in self.inventory.values()):
            raise ValueError("Quantidade de inventário negativa")
