def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(",")
                total += int(salary)
                count += 1

        average = total / count if count > 0 else 0

        return total, average

    except FileNotFoundError:
        return "Файл не знайдено"
    except Exception as error:
        return f"Сталася помилка: {error}"


def get_cats_info(path):
    cats_info = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")

                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats_info.append(cat)

        return cats_info

    except FileNotFoundError:
        return "Файл не знайдено"
    except Exception as error:
        return f"Сталася помилка: {error}"


from pathlib import Path
from colorama import Fore, Style, init
import sys

init(autoreset=True)


def print_directory_structure(path, indent=""):
    try:
        for item in path.iterdir():

            if item.is_dir():
                print(Fore.BLUE + indent + f"📂 {item.name}")
                print_directory_structure(item, indent + "    ")

            else:
                print(Fore.GREEN + indent + f"📜 {item.name}")

    except Exception as error:
        print(Fore.RED + f"Помилка: {error}")


def main_directory():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до директорії")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print(Fore.RED + "Шлях не існує")
        return

    if not path.is_dir():
        print(Fore.RED + "Це не директорія")
        return

    print(Fore.YELLOW + f"Структура директорії: {path}")
    print_directory_structure(path)


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone

    return "Контакт додано."


def change_contact(args, contacts):
    name, phone = args

    if name in contacts:
        contacts[name] = phone
        return "Контакт оновлено."

    return "Контакт не знайдено."


def show_phone(args, contacts):
    name = args[0]

    if name in contacts:
        return contacts[name]

    return "Контакт не знайдено."


def show_all(contacts):
    if not contacts:
        return "Контакти відсутні."

    result = ""

    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"

    return result.strip()


def main():
    contacts = {}

    print("Вітаємо у боті-помічнику!")

    while True:
        user_input = input("Введіть команду: ")

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("До побачення!")
            break

        elif command == "hello":
            print("Чим я можу вам допомогти?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Невірна команда.")


if __name__ == "__main__":
    main()