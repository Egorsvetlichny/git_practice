"""
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths.
Can you help him find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and
returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts
(e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects,
can be considered as 0.

Examples:
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 2
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
# must return 0
"""


# my solution
def count_available_cakes(recipe: dict, available: dict) -> int:
    min_cakes = []

    for key, value in recipe.items():
        if key not in available:
            return 0

        min_cakes.append(available[key] // value)

    return min(min_cakes) if min_cakes else 0


# best solution
def cakes(recipe: dict, available: dict) -> int:
    return min([available[key] // recipe[key] if key in available else 0 for key in recipe]) if recipe else 0


def main():
    assert count_available_cakes({"flour": 500, "sugar": 200, "eggs": 1},
                                 {"flour": 1200, "sugar": 1200, "eggs": 5, 'milk': 200}) == 2
    assert count_available_cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
                                 {"sugar": 500, "flour": 2000, "milk": 2000}) == 0
    assert count_available_cakes({}, {}) == 0
    assert count_available_cakes({}, {"sugar": 500, "flour": 2000, "milk": 2000}) == 0
    assert count_available_cakes({"sugar": 500, "flour": 2000, "milk": 2000}, {}) == 0


if __name__ == '__main__':
    main()
