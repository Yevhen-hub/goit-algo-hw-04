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
        print("Файл не знайдено.")
        return 0, 0

    except Exception as error:
        print(f"Сталася помилка: {error}")
        return 0, 0


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}")
print(f"Середня заробітна плата: {average}")

def get_cats_info(path):
    cats_info = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")

                cat_dict = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats_info.append(cat_dict)

        return cats_info

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []

    except Exception as error:
        print(f"Сталася помилка: {error}")
        return []


cats_info = get_cats_info("cats_file.txt")
print(cats_info)