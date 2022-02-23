import subprocess
import os


class EpicCmd:
    def __init__(self, lgndry):
        self.lgndry = lgndry

    def launch_process(self, params=None, *args):
        if params is None:
            params = []
        if isinstance(params, str):
            params = [params]
        params.extend(args)
        return subprocess.Popen([self.lgndry, *params],
                                stdout=subprocess.PIPE,
                                stdin=subprocess.PIPE)


class Auth:
    def __init__(self, epic_cmd):
        self.cmd = epic_cmd

    def login(self, sid=None):
        def send_sid(sid, process, stdout, self):
            process.communicate(input=bytes(sid + "\n", "utf-8"))
            while process.poll() is None:
                try:
                    print(next(stdout))
                except ValueError:
                    pass
            return {
                "id": "logged"
            }

        process = self.cmd.launch_process("auth")
        stdout = iter(process.stdout.readline, b"")
        try:
            if next(stdout) == b'Please login via the epic web login!\r\n':
                if sid is None:
                    return {
                        "id": "login_sid",
                        "function": lambda sid, process=process, stdout=stdout, sel=self:
                        send_sid(sid, process, stdout, sel),
                        "url": "".join(list(str(next(stdout)).split(" ")[-1])[0:-5])
                    }
                else:
                    return send_sid(sid, process, stdout, self)
        except StopIteration:
            if os.path.isfile(os.path.join(os.getcwd(), "config/legendary/user.json")):
                return {
                    "id": "logged"
                }
            else:
                return {
                    "id": "false_sid"
                }
