from pathlib import Path
from colorama import init, Fore
import sys

init(autoreset=True)


def draw_directory(path, indent=""):
    for item in path.iterdir():
        if item.is_dir():
            print(Fore.BLUE + indent + f"📂 {item.name}")
            draw_directory(item, indent + "    ")
        else:
            print(Fore.GREEN + indent + f"📜 {item.name}")


def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до директорії.")
        return

    directory = Path(sys.argv[1])

    if not directory.exists():
        print("Шлях не існує.")
        return

    if not directory.is_dir():
        print("Це не директорія.")
        return

    print(Fore.YELLOW + f"📦 {directory.name}")
    draw_directory(directory)


if __name__ == "__main__":
    main()