import os
def linux():
  os.system("clear")
  while True:
       # os.system("clear")
        print("Local system basic linux commands\n\nPress the respective key to run the commands\n\nPress 1 : To run the date command\nPress 2 : To see the calender command\nPress 3 : To see the ip address\nPress 4 : To exit\n")
        linux_key = input("\nEnter your choice : ")
        if linux_key=="1":
            os.system("date")
        elif linux_key=="2":
            os.system("cal")
        elif linux_key=="3":
            os.system("ifconfig")
        elif linux_key=="4":
            exit()
        else:
            print("\nWrong Input !!!")
       # input()
       # input("\nEnter to continue...")
