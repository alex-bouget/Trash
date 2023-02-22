import configparser
from hashlib import md5
from simplecrypt import encrypt, decrypt
import json
import os
from tempfile import tempdir

def encode(config_file, plugin_path, file_path):
    """Encode plugins."""
    config = configparser.ConfigParser()
    config.read(config_file)
    plugins = os.listdir(plugin_path)
    key_decoded = json.loads(config["Api"]["krom_id"])
    key = bytes(md5(str(key_decoded).encode("utf-8")).hexdigest(), "utf-8")
    data = b""
    for plugin in plugins:
        if plugin.endswith(".py"):
            data += b"\n" + bytes(key) + b"\n" 
            temp = open(os.path.join(plugin_path, plugin), "rb").read()
            data += temp
    file = open(file_path, "wb")
    file.write(encrypt(key, data))
    file.close()
encode("kromblast.ini", "plugins", "file.kbp")