from pathlib import Path

current_dir = Path(__file__).parent


def get_cats_info(path: str) -> list[dict[str, int]]:

    # gather the data
    with open(current_dir / path, "r", encoding="utf-8") as fl:
        data = fl.readlines()
    # define the list to store dicts
    cats_list = []

    # create dicts with data
    for el in data:
        cat_id, name, age = el.split(",")
        cat_dict = {"id": cat_id, "name": name, "age": age.strip()}
        cats_list.append(cat_dict)
    return cats_list


print(get_cats_info("cats.txt"))
