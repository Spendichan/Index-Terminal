import time
from pathlib import Path


def ls():
    path = Path(input("\npath: "))
    if not path.is_dir():
        print(f"\npath: {path} not found")
    for file in path.rglob("*"):
        print(file)

def main(command):
    match command:
        case "ls":
            ls()

        case "help":
            print("""
help                -shows all available commands
hardware-monitor    -monitor your hardware
ls                  -list every file/folder in a path
exit                -exit the Index Terminal
""")

        case "exit":
            print("\nGoodbye.")
            time.sleep(2)
            return 0

        case "hardware-monitor":
            #hardware_monitor.main()
            print("\ncommand not done yet")

        case "":
            print("\nplease enter a command")

        case _:
            print(f"\nunknown command: {command}")

print("""
----------------
 Index Terminal
----------------
-type in "help"-
""")

while True:
    command = input(f"\n{time.ctime()} : > ")
    check = main(command)
    if check == 0:
        break
