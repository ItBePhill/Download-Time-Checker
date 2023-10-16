#Imports
import time
import datetime
import math
#Download Time Checker
#Written by Phill

#Var
startorstop = 0
speed = None
sure =  None
size = None
def Startup():
    print("----- Welcome to the Download Time Checker -----")
    print("Would Would you Like to do?:\n1: Start\n2: Quit")
    while True:
        startorstop = int(input("- "))
        if startorstop not in [1, 2]:
            print("Error: Invalid Response")
            continue
        
        elif startorstop == 1:
            DownloadCheckerStart()
            break

        else:
            quit(0)


def DownloadCheckerStart():
    def Calculate(speed, size):
        Totalunform = round((size * 1000000000) / ((speed * 1000000) / 8))

        Totalform = datetime.timedelta(seconds = Totalunform)
        return Totalform

    print("---- Download Time Checker ----")
    while True:
        speed = input("Input your download speed in mbps(megabits per second): If you are unsure visit: https://www.speedtest.net/\n- ")
        sure = input("Are you sure? (y/n)\n- ")
        if sure not in ["y", "n"]:
            print("Error: invalid response")

        elif sure == "y":
            break
        
        else:
            print("\n")
            continue


    while True:
        size = input("Input the size of the file you are downloading in GB(Gigabytes)\n- ")
        sure = input("Are you sure? (y/n)\n- ")
        if sure not in ["y", "n"]:
            print("Error: invalid response")

        elif sure == "y":
            sure = None
            print("Calculating the Result...\n")
            time.sleep(1)
            break
            
        
        else:
            print("\n")
            continue

    print(f"The Result is: {Calculate(float(speed), float(size))}")


Startup()