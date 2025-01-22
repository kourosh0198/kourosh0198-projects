import time
import os

time_input = int(input("Enter the time per secend: "))

while time_input >= 0:
    print(time_input)
    time_input -= 1
    time.sleep(1)
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

