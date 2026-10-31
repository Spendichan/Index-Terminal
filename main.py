import time
from pathlib import Path

from hardware_monitor import check_hardware


def ls():
    path = Path(input("\npath: ")).expanduser()

    if not path.is_dir():
        print(f"\nPath not found or not a directory: {path}")
        return

    for file in sorted(path.iterdir()):
        if file.is_dir():
            print(f"[DIR]  {file.name}")
        else:
            print(f"[FILE] {file.name}")


def main(command):
    match command:
        case "ls":
            ls()

        case "help":
            print("""
help                - Show all available commands
hardware-monitor    - Monitor your hardware
ls                  - List files and folders in a path
exit                - Exit the Index Terminal
""")

        case "exit":
            print("\nGoodbye.")
            time.sleep(1)
            return 0

        case "hardware-monitor":
            print("\navailable commands: ram, cpu, disk, exit")
            check_hardware()

        case "":
            print("\nPlease enter a command.")

        case _:
            print(f"\nUnknown command: {command}")


print("""
----------------
 Index Terminal
----------------
Type "help" to see commands
""")

while True:
    command = input(f"\n{time.ctime()} : > ").strip()
    check = main(command)

    if check == 0:
        break
