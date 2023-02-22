import json
import os

lang = ""


def getlang():
    return json.load(open(os.path.join("Ressources", "lang", lang + ".json")))
