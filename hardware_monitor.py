import psutil

def check_hardware():
    command = input("\n>")
    print("")

    if command == ("cpu"):
        print(f"CPU usage: {psutil.cpu_percent(interval = 1)} %")
    elif command == ("ram"):
        print(f"RAM total: {round(psutil.virtual_memory().total / 1024**3, 2)} GB")
        print(f"RAM used: {round(psutil.virtual_memory().used / 1024**3, 2)} GB")
        print(f"RAM available: {round(psutil.virtual_memory().available / 1024**3, 2)} GB")
        print(f"RAM usage: {round(psutil.virtual_memory().percent)} %")
    elif command == ("disk"):
        try:
            print(f"Disk total: {round(psutil.disk_usage("C://").total / 1024**3, 2)} GB")
            print(f"Disk usage: {round(psutil.disk_usage("C://").used / 1024**3, 2)} GB")
            print(f"Disk available: {round(psutil.disk_usage("C://").free / 1024**3, 2)} GB")
        except:
            print(f"Disk total: {round(psutil.disk_usage("/").total / 1024**3, 2)} GB")
            print(f"Disk usage: {round(psutil.disk_usage("/").used / 1024**3, 2)} GB")
            print(f"Disk available: {round(psutil.disk_usage("/").free / 1024**3, 2)} GB")
    elif command == ("exit"):
        print("\nexiting hardware monitor.")
        return 
    else:
        print(f"\nunknown command: {command}")

    check_hardware()
