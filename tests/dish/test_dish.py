import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient


# Req 2
def test_dish():
    Hamburguer = "Hamburguer"
    Pizza = "Pizza"

    Hamburguer_instance = Dish(Hamburguer, 79.90)
    Pizza_instance = Dish(Pizza, 69.90)

    assert Hamburguer_instance.name == Hamburguer
    assert Hamburguer_instance == Hamburguer_instance
    assert Hamburguer_instance != Pizza_instance
    assert hash(Hamburguer_instance) == hash(repr(Hamburguer_instance))
    assert repr(Hamburguer_instance) == f"Dish('{Hamburguer}', R$79.90)"

    Hamburguer_instance.add_ingredient_dependency(Ingredient("Ovo"), 1.90)

    assert Hamburguer_instance.recipe == {Ingredient("Ovo"): 1.90}
    assert Hamburguer_instance.get_ingredients() == set(
        Hamburguer_instance.recipe.keys()
    )
    assert Hamburguer_instance.get_restrictions() == set()

    FLOAT_ERROR = "Dish price must be float."
    PRICE_GT_ZERO_ERROR = "Dish price must be greater then zero."

    with pytest.raises(TypeError, match=FLOAT_ERROR):
        Dish(Hamburguer, "79,90")
    with pytest.raises(ValueError, match=PRICE_GT_ZERO_ERROR):
        Dish(Hamburguer, -9)
    with pytest.raises(ValueError, match=PRICE_GT_ZERO_ERROR):
        Dish(Hamburguer, 0)
    with pytest.raises(ValueError, match=PRICE_GT_ZERO_ERROR):
        Dish(Hamburguer, 0.0)
