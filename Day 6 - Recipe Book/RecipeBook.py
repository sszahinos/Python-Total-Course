from os import system
from pathlib import Path

main_path = Path("Recipes")
all_categories = ["Meat", "Salad", "Pasta", "Dessert"]

default_meat = ["Chicken Drumstick", "Prosciuto Pizza"]
default_meat_text = ["Chicken Drumstick text", "Prosciuto Pizza text"]

default_salad = ["Caesar"]
default_salad_text = ["Caesar text"]

default_pasta = ["Penne", "Spaghetti"]
default_pasta_text = ["Penne text", "Spaghetti text"]

default_dessert = ["Yogurt", "Cheesecake", "Jelly"]
default_dessert_text = ["Yogurt text", "Cheesecake text", "Jelly text"]


def start_program():
    end = False
    # Create directories and default files if not exists and the program has not been used ever.
    if not main_path.exists():
        create_default_content()
    global all_categories
    all_categories = get_categories()
    # Greetings
    print("Welcome to your Recipes Book. Currently you have:")

    # Tell where the folders are located and how many recipes has inside.
    show_all()

    print("--------------")
    while not end:
        option = ""
        # Ask for an option
        option_correct = False
        while not option_correct:
            show_menu()
            option = ask_option()
            option_correct = check_option(option)
            clear()
            if not option_correct:
                print("Wrong option.")

        if option == "1":  # 1 - Read recipe
            # Ask category
            show_categories()
            category = all_categories[int(ask_category()) - 1]
            if len([item for item in Path(main_path, category).glob("*")]) == 0:
                clear()
                print("This category is empty")
            else:
                # Ask recipe
                recipes = find_recipes(category)
                option_correct = False
                while not option_correct:
                    show_recipes(recipes)
                    option = ask_recipe()
                    option_correct = check_recipe(recipes, option)
                    if not option_correct:
                        clear()
                        print("Wrong option")

                # Show recipe
                recipe = recipes[int(option) - 1]
                show_recipe(category, recipe)
                input("Press any key to continue")
                clear()
        elif option == "2":  # 2 - Create recipe
            # Ask category
            show_categories()
            category = all_categories[int(ask_category()) - 1]

            # Ask for a new recipe
            new_recipe = ask_new_recipe()
            create_recipe(new_recipe[0], new_recipe[1], category)

            print("Recipe created.")
            input("Press any key to continue")
            clear()
        elif option == "3":  # 3 - Create category
            category = ask_new_category()
            create_category(category)

            print("Category created.")
            input("Press any key to continue")
            clear()
        elif option == "4":  # 4 - Delete recipe
            # Ask category
            show_categories()
            category = all_categories[int(ask_category()) - 1]
            if len([item for item in Path(main_path, category).glob("*")]) == 0:
                clear()
                print("This category is empty")
            else:
                # Ask recipe
                recipes = find_recipes(category)
                option_correct = False
                while not option_correct:
                    show_recipes(recipes)
                    option = ask_recipe()
                    option_correct = check_recipe(recipes, option)
                    if not option_correct:
                        clear()
                        print("Wrong option")

                # Delete recipe
                recipe = recipes[int(option) - 1]
                delete_recipe(recipe, category)

                print("Recipe deleted.")
                input("Press any key to continue")
                clear()
        elif option == "5":  # 5 - Delete category
            # Ask category
            show_categories()
            category = all_categories[int(ask_category()) - 1]

            delete_category(category)

            print("Category deleted.")
            input("Press any key to continue")
            clear()
        elif option == "6":  # 6 - Exit
            print("Have a nice day!")
            end = True


###################

def clear():
    system("cls")


def get_categories():
    return [recipe.name for recipe in main_path.glob("*")]


def show_menu():
    print("""--- MAIN MENU ---
1. Show recipe
2. Create recipe
3. Create category
4. Delete recipe
5. Delete category
6. Close Recipes Book""")


def show_categories():
    print("Categories\n----------")
    global all_categories
    for index, cat in enumerate(all_categories):
        print(f"{index + 1}. {cat}")


def show_recipes(recipes):
    for index, recipe in enumerate(recipes):
        print(f"{index + 1}. {recipe}")


def show_recipe(category, recipe):
    file = Path(main_path, category, recipe + ".txt").open(mode="r")
    print(file.read())


def show_all():
    global all_categories
    for categories in main_path.glob('*'):
        print("|-\t" + categories.name)
        for recipes in categories.glob('*'):
            print("|\t|- \t" + recipes.stem)


def find_recipes(category):
    cat_path = Path(main_path, category)
    return [recipe.stem for recipe in cat_path.glob("*")]


def check_option(option):
    its_ok = False
    if option.isnumeric() and 0 < int(option) < 7:
        its_ok = True
    return its_ok


def check_recipe(recipes, option):
    its_ok = False
    if option.isnumeric() and int(option) in range(1, len(recipes) + 1):
        its_ok = True
    return its_ok


def check_category(option):
    is_correct = False
    if option.isnumeric() and int(option) in range(1, len(all_categories) + 1):
        is_correct = True

    return is_correct


def ask_option():
    return input("Select an option -> ")


def ask_category():
    option = ""
    is_correct = False
    while not is_correct:
        option = input("Choose a category --> ")
        if not check_category(option):
            print("Wrong category.")
        else:
            is_correct = True

    return option


def ask_recipe():
    return input("Choose a recipe: ")


def ask_new_recipe():
    title = input("Recipe's title --> ")
    text = input("Recipe's content:\n")
    return [title, text]


def ask_new_category():
    return input("New category's name --> ")


def delete_category(category):
    global all_categories
    category_path = Path(main_path, category)
    for recipe in Path(category_path).glob("*.txt"):
        delete_recipe(recipe.stem, category)
    category_path.rmdir()
    all_categories = get_categories()


def delete_recipe(recipe, category):
    print(recipe)
    recipe_path = Path(main_path, category, recipe + ".txt")
    recipe_path.unlink()


def create_category(category):
    global all_categories
    category_path = Path(main_path, category)
    try:
        category_path.mkdir()
        all_categories = get_categories()
    except FileExistsError:
        print("Category already exists.")


def create_recipe(recipe_name, text, category):  # Also overwrites
    recipe_path = Path(main_path, category, recipe_name + ".txt")
    file = recipe_path.open(mode="w")
    file.write(text)


def create_default_content():
    main_path.mkdir()
    for category in all_categories:
        create_category(category)
        if category == all_categories[0]:  # Meat
            for index, meat in enumerate(default_meat):
                create_recipe(meat, default_meat_text[index], category)
        elif category == all_categories[1]:  # Salad
            for index, salad in enumerate(default_salad):
                create_recipe(salad, default_salad_text[index], category)
        elif category == all_categories[2]:  # Pasta
            for index, pasta in enumerate(default_pasta):
                create_recipe(pasta, default_pasta_text[index], category)
        elif category == all_categories[3]:  # Dessert
            for index, dessert in enumerate(default_dessert):
                create_recipe(dessert, default_dessert_text[index], category)


###
start_program()