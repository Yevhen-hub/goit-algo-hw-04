from pathlib import Path
import sys

def total_salary(path):
    total = 0
    count = 0
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            _, salary = line.strip().split(",")
            total += int(salary)
            count += 1
    return (total, total / count) if count else (0, 0)

def get_cats_info(path):
    result = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            cat_id, name, age = line.strip().split(",")
            result.append({"id": cat_id, "name": name, "age": age})
    return result

def print_tree(path, indent=""):
    for item in path.iterdir():
        if item.is_dir():
            print(indent + f"📂 {item.name}")
            print_tree(item, indent + "    ")
        else:
            print(indent + f"📄 {item.name}")

def run_directory():
    if len(sys.argv) < 2:
        print("Вкажіть шлях")
        return
    path = Path(sys.argv[1])
    if not path.exists() or not path.is_dir():
        print("Некоректний шлях")
        return
    print_tree(path)

def parse_input(user_input):
    parts = user_input.split()
    return parts[0].lower(), parts[1:]

def run_bot():
    contacts = {}
    while True:
        command, args = parse_input(input(">>> "))
        if command in ["exit", "close"]:
            break
        elif command == "add":
            contacts[args[0]] = args[1]
            print("Контакт додано")
        elif command == "change":
            if args[0] in contacts:
                contacts[args[0]] = args[1]
                print("Оновлено")
            else:
                print("Не знайдено")
        elif command == "phone":
            print(contacts.get(args[0], "Не знайдено"))
        elif command == "all":
            print(contacts)
        elif command == "hello":
            print("Привіт")
        else:
            print("Невідома команда")

if __name__ == "__main__":
    print("1 - directory")
    print("2 - bot")
    choice = input(">>> ")
    if choice == "1":
        run_directory()
    elif choice == "2":
        run_bot()