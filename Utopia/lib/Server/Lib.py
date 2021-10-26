from threading import Thread
import json
from requests import get, post


class Server(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.System = json.loads(get(self.url, {"MM1_jc": "200"}).text)
        self.daemon = True
        self.thread_return = []
        self.thread_send = []

    def getJsBySystem(self, name, post_data={}):
        def getUrl(url, get_data):
            data_get = []
            for key, value in get_data.items():
                data_get.append(key + "=" + value)
            return url + "?" + "&".join(data_get)
        resolve = post(getUrl(self.url, self.System[name]["GET"]), data=post_data).text
        print(resolve)
        return json.loads(resolve)

    def ThreadReturn(self):
        if len(self.thread_return) == 0:
            msg = None
        else:
            msg = self.thread_return[0]
            del self.thread_return[0]
        return msg

    def GetSend(self):
        while len(self.thread_send) == 0:
            pass
        msg = self.thread_send[0]
        del self.thread_send[0]
        return msg

    def ThreadSend(self, msg):
        self.thread_send.append(msg)
