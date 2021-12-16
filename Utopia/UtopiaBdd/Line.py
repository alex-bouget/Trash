import sys
import os


def start():
    print(sys.argv)
    if sys.argv[1] == "open":
        if os.path.isdir(sys.argv):
            print("1")
    elif sys.argv[1] == "create":
        print("k")