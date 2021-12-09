#-------------------------------------------------------------------------------
# Name:        Video
# Purpose:     Script For Relic_Engine
#
# Author:      MisterMine01
#
# Created:     26/03/2020
# Copyright:   (c) MisterMine01 2020
#-------------------------------------------------------------------------------
exec("import os\nimport vlc\nimport pafy\nimport threading", globals())
def play_video(self, path):
    def video_thread_stop(self):
        time.sleep(3)
        for i in range(self.player.get_length()):
            time.sleep(0.1)
            if self.player.is_playing() == False:
                break
        self.stop_video()
    self.video_canvas = Canvas(self, width=self.w,height=self.h)
    self.video_canvas.place(x=0, y=0)
    self.instance = vlc.Instance()
    self.player = self.instance.media_player_new()
    self.player.set_hwnd(self.video_canvas.winfo_id())
    self.player.set_media(self.instance.media_new(path))
    self.unbind_all()
    self.player.play()
    self.stop_system_list.append(self.player.stop)
    threading.Thread(target=lambda: video_thread_stop(self)).start()
    self.root.mainloop()
def stop_video(self, *evt):
    self.root.unbind("<Return>")
    self.using = False
    self.video_canvas.destroy()
    self.player.stop()
    self.rebind_all()
    self.root.quit()
def play_video_url(self, path):
    self.play_video(pafy.new(path).getbest().url)