#Imports
import time
import datetime
#Download Time Checker V0.1
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

        

    print("---- Download Time Checker ----")
    while True:
        speed = input("Input your download speed: If you are unsure visit: https://www.speedtest.net/\n- ")
        sure = input("Are you sure? (y/n)\n- ")
        if sure not in ["y", "n"]:
            print("Error: invalid response")

        elif sure == "y":
            break
        
        else:
            print("\n")
            continue


    while True:
        size = input("Input the size of the file you are downloading\n- ")
        sure = input("Are you sure? (y/n)\n- ")
        if sure not in ["y", "n"]:
            print("Error: invalid response")

        elif sure == "y":
            sure = None
            break
        
        else:
            print("\n")
            continue


    print(f"The Results are: {Calculate(speed, size)}")


Startup()