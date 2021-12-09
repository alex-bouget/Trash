"php server protocol by MisterMine01"
import requests
class API:
    def __init__(self, adress):
        """
        Server Protocol MisterMine01 V1 API
        """
        self.adress = adress
    def connect(self, **kwargs):
        r = requests.get(url = self.adress, params=kwargs)
        if str(r)=="<Response [500]>":
            raise OSError("Server Problem, Contact Moderator")
        if r.text=="":
            raise ValueError("parameter missing or connection missing")
        print(r)
        print(r.text)
        print("---------------------")
        return r.json()