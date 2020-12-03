from itertools import groupby
from typing import Union


def get_file_lines(file_name: str) -> list:
    with open(file_name, ) as source:
        file_contents = [line.replace('\n', '') for line in source.readlines()]
        return file_contents


def _split_into_recipes(file_data: list) -> list:
    # разбиваем содержимое полученное содержимое файла
    # на лист листов, где каждый лист - данные рецепта

    recipes = [list(g) for k, g in groupby(file_data, lambda x: x=='') if
               not k]

    return recipes


def _format_ingredient_value(val: str) -> Union[str, int]:
    formatted = val.strip()
    if formatted.isnumeric():
        return int(formatted)
    return formatted


def _format_ingredient(ingredient: list) -> list:
    return [_format_ingredient_value(el) for el in ingredient.split('|')]


def parse_cookbook(file_name: str):
    result = {}
    ingredient_keys = ['ingredient_name', 'quantity', 'measure']
    # может быть константой, но по условию глобальные переменные запрещены

    file_data = get_file_lines(file_name)
    recipes = _split_into_recipes(file_data)

    for dish in recipes:
        dish_name = dish[0]
        ingredient_count = int(dish[1])

        result[dish_name] = []

        for ingredient in dish[-ingredient_count:]:
            formatted = _format_ingredient(ingredient)

            recipe_ingredient = {k: v for k, v in zip(ingredient_keys, formatted)}
            result[dish_name].append(recipe_ingredient)

    return result


result = parse_cookbook('recipes.txt')
print(result)



