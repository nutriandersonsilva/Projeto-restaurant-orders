from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
import pytest


def test_dish():
    dish1 = Dish("Macarrão Carbonara", 15.00)
    dish2 = Dish("Lasanha", 20.00)
    dish3 = Dish("Pizza Margherita", 18.00)

    ingredient1 = Ingredient("bacon")
    ingredient2 = Ingredient("queijo parmesão")
    ingredient3 = Ingredient("molho branco")

    assert dish1.name == "Macarrão Carbonara"
    assert dish1.price == 15.00
    assert dish1.recipe == {}

    assert dish1.__repr__() == "Dish('Macarrão Carbonara', R$15.00)"
    assert dish1.__repr__() == dish2.__repr__()
    assert dish1.__repr__() != dish3.__repr__()

    assert dish1 == dish2
    assert dish1 != dish3

    assert dish1.__eq__(dish2) is True
    assert dish1.__eq__(dish3) is False

    assert dish1.__hash__() == dish2.__hash__()
    assert dish1.__hash__() != dish3.__hash__()

    dish1.add_ingredient_dependency(ingredient1, 2)
    dish1.add_ingredient_dependency(ingredient2, 3)
    dish2.add_ingredient_dependency(ingredient3, 4)

    assert dish1.get_ingredients() == {ingredient1, ingredient2}
    assert dish1.recipe == {ingredient1: 2, ingredient2: 3}

    assert dish1.get_restrictions() == {
        Restriction.GLUTEN,
        Restriction.ANIMAL_DERIVED
    }

    with pytest.raises(ValueError):
        Dish("Macarrão Carbonara", 0)

    with pytest.raises(TypeError):
        Dish("Macarrão Carbonara", "15")
