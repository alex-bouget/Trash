from epic import Auth
from epic import EpicCmd
import sys

file, first = sys.argv

if first == "auth":
    epic = Auth(EpicCmd("Legendary"))
    ret = epic.login()
    while True:
        if ret["id"] == "login_sid":
            print("Not authenticated, enter sid")
            ret = ret["function"](input("sid: "))
        elif ret["id"] == "false_sid":
            print("Not authenticated, false sid")
            break
        elif ret["id"] == "logged":
            print("Authenticated")
            break

