from os import system

def clear():
    system("cls")

def show_menu():
    print("""--- MAIN MENU ---
    1. Show recipe
    2. Create recipe
    3. Create category
    4. Delete recipe
    5. Delete category
    6. Close Recipes Book""")

def show_categories():
    pass

def show_recipes(category):
    pass

def check_category(category):
    its_ok = False
    if category.isnumeric() and 0 < category < 7:
        its_ok = True
    return its_ok

def check_recipe(recipe):
    pass

def ask_category():
    option = -1
    while not check_category(option):
        print("Choose a category:")
        show_categories()
        option = input()

    return option

def ask_recipe():
    return input("Choose a recipe: ")

def delete_category(category):
    pass

def delete_recipe(recipe):
    pass

def create_default_directories():
    pass

# Create directories if not exists

# Greetings
print("Welcome to your Recipes Book")
# Tell where the folders are located and how many recipes has inside.

# Show menu
# 1 - Read recipe
# Ask category
# Ask recipe
# Show recipe

# 2 - Create recipe
# Ask category
# Ask recipe name
# Ask content
# Create content

# 3 - Create category
# Ask category
# Create category

# 4 - Delete recipe
# Ask category
# Ask recipe
# Delete recipe

# 5 - Delete category
# Ask category
# Delete category

# 6 - End program