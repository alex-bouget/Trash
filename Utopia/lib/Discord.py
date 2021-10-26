from discordsdk import *
from threading import Thread
import logging
import time


class DiscordLib:
    def __init__(self):
        self._discord = Discord(829343636994261032, CreateFlags.default)
        self._activity = Activity()
        self.thread = Thread(target=self.thread_using, daemon=True)
        self.thread.start()
        self._activity.assets.large_image = "icone2-1024"
        self._activity.timestamps.start = time.time()

    def thread_using(self):
        while 1:
            time.sleep(1 / 10)
            self._discord.run_callbacks()

    def update_activity(self):
        def callback(result):
            if result == Result.ok:
                logging.debug("Discord activity reset")
            else:
                raise Exception(result)

        self._discord.get_activity_manager().update_activity(self._activity, callback)

    def change_activity(self, **kwargs):
        self._activity.state = kwargs.get("state", "On menu")
        self.update_activity()
