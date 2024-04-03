from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
import pytest


def test_dish():
    dish1 = Dish("lasanha", 10.50)
    dish2 = Dish("lasanha", 10.50)
    dish3 = Dish("Pizza", 15.00)

    ingredient1 = Ingredient("ovo")
    ingredient2 = Ingredient("farinha")

    assert dish1.name == "lasanha"
    assert dish1.price == 10.50
    assert dish1.recipe == {}

    assert dish1.__repr__() == "Dish('lasanha', R$10.50)"
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

    assert dish1.get_ingredients() == {ingredient1, ingredient2}
    assert dish1.recipe == {ingredient1: 2, ingredient2: 3}

    assert dish1.get_restrictions() == {
        Restriction.GLUTEN,
        Restriction.ANIMAL_DERIVED
    }

    with pytest.raises(ValueError):
        Dish("lasanha", 0)

    with pytest.raises(TypeError):
        Dish("lasanha", "10")
