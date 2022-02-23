from MariusLauncher.extensions.extensions_loader import Extension
"""
epic = Extension("epic.efs")
load = epic.launch_process("auth")
stdout = iter(load.stdout.readline, b"")
for i in stdout:
    print(i)
load.communicate(input=bytes(input("sid: ") + "\n", "utf-8"))

"""
from MariusLauncher.decompiler import Decompiler
from MariusLauncher.Windows import Windows
import json

root = Windows()
root.configure(height=480, width=720)
rt = Decompiler()

js = json.load(open("page.json"))

rt.load_json(root, js)

root.mainloop()
