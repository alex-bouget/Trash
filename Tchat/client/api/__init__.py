from .api import API
from .client_compiler import compiler
import requests
import os

def launch_api(server):
    compi = compiler(requests.get(url=os.path.join(server, "data.json")).text)
    compi.compile("temp")
    exec(open("temp").read(), globals())
    return App_Api(server)