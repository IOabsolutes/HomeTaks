from pathlib import Path

current_dir = Path(__file__).parent


def total_salary(path: str) -> tuple[int]:
    try:
        # open file and gather the data from it
        with open(current_dir / path, "r", encoding="utf-8") as fl:
            data = fl.readlines()
        # define lists to separete data
        list_of_employes = []
        salary_list = []
        # go throught the list
        for el in data:
            # splict the element and unpack it into varibles
            dev, salary = el.split(",")
            # add them to relevant lists
            list_of_employes.append(dev)
            salary_list.append(int(salary))
        # calculate total via avarage salaries
        total = sum(salary_list)
        avarage = int(total / len(list_of_employes))
        return total, avarage
    except FileExistsError:
        print("Sorry file doesn't exist")


print(total_salary("salary.txt"))
