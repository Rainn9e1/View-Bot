import requests, datetime, json, random, warnings, os, threading, time
from colorama import *
from requests.sessions import Session

init()

def warn(*args, **kwargs):
    pass

warnings.warn = warn

class Library:
    Name = "9e1 Github View Botter"

    class Json:
        def Read(FileName, Key):
            File = open(FileName, "r")
            Data = json.loads(File.read())

            return Data[Key]

    def Print(message, mode = None, title = None):
        Hour = int(datetime.datetime.now().strftime("%H")) - 12
        Minute = int(datetime.datetime.now().strftime("%M"))

        if len(str(Minute)) < 2:
            Minute = f"0{Minute}"

        if not mode == None:
            if str.lower(mode) == "warning":
                Theme = Fore.YELLOW
                Title = "WARNING"
            elif str.lower(mode) == "normal":
                Theme = Fore.LIGHTBLUE_EX
                Title = Library.Name
            elif str.lower(mode) == "error":
                Theme = Fore.LIGHTRED_EX
                Title = "ERROR"
        else:
            Theme = Fore.LIGHTBLUE_EX
            Title = Library.Name
            
        if not title == None:
            Title = title
            
        Time = f"{Hour}:{Minute}".replace("-", "")
        
        Callback = print(f"  {Fore.WHITE}{Time}{Fore.RESET} | {Theme}{Title}{Fore.RESET} | {Fore.LIGHTWHITE_EX}{message}{Fore.RESET}")
        
        return Callback

    def Input(message, mode = None, title = None):
        Hour = int(datetime.datetime.now().strftime("%H")) - 12
        Minute = int(datetime.datetime.now().strftime("%M"))

        if len(str(Minute)) < 2:
            Minute = f"0{Minute}"

        if not mode == None:
            if str.lower(mode) == "warning":
                Theme = Fore.YELLOW
                Title = "WARNING"
            elif str.lower(mode) == "normal":
                Theme = Fore.LIGHTBLUE_EX
                Title = Library.Name
            elif str.lower(mode) == "error":
                Theme = Fore.LIGHTRED_EX
                Title = "ERROR"
        else:
            Theme = Fore.LIGHTBLUE_EX
            Title = Library.Name
            
        if not title == None:
            Title = title
            
        Time = f"{Hour}:{Minute}".replace("-", "")
        
        Callback = input(f"  {Fore.WHITE}{Time}{Fore.RESET} | {Theme}{Title}{Fore.RESET} | {Fore.LIGHTWHITE_EX}{message}{Fore.RESET}: ")
        
        return Callback

os.system("cls")
os.system("title "+ f"{Library.Name}")

TargetURL = ""
Views = 0

Session = requests.Session()

def View(ID):
    global Views

    Request = Session.get(str(ID),
        json = {
            "Nothing": "Null"
        }, 
        
        headers = {
            "user-agent": Library.Name
        }
    )

    if Request.status_code == 200:
        Views = Views + 1

        os.system("cls")

        Library.Print(f"Added View: {Views}", "normal")
        Library.Print(f"Module Activity : True", "normal")

        os.system("title "+ f"{Library.Name} * {Views}")
        
def __Start():
    global TargetURL
        
    while True:
        View(TargetURL)

Library.Print("Loaded Modules | Created by  9e1 (Rainn)", "normal")

TargetURL = Library.Input("Target (READ README.MD TO GET TARGET URL)")
Threads = int(Library.Input("Threads (Max 10 : Min 1)"))

if Threads > 10 or Threads < 1:
    Threads = 5

for _threaded in range(Threads):
    threading.Thread(target = __Start).start()
