from .Relic import Relic


class Main:
    relic_engine = Relic()
    windows = relic_engine.master
    y = windows.winfo_y()  # height
    x = windows.winfo_x()  # width


class Camera:
    cam_x = 0
    cam_y = 0

    @staticmethod
    def reload_camera():
        Camera.cam_x = Main.relic_engine.winfo_width()//2
        Camera.cam_y = Main.relic_engine.winfo_height()//2
