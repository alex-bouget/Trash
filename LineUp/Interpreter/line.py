class Line:
    def __init__(self, line):
        self.line = line
        self.comment = False
        self.decoded_line = self.decode_line()

    def get_sub_line(self):
        entry_indices = [i for i, x in enumerate(self.line) if x == "("]
        close_indices = [i for i, x in enumerate(self.line) if x == ")"]

        finish = []
        for i in range(len(entry_indices)):
            finish.append(entry_indices[i])
            finish.append(close_indices[i])
            if i != 0 and finish[-3] > finish[-2]:
                del finish[-2]
                del finish[-2]
        return finish

    def decode_line(self):
        sub = self.get_sub_line()
        splited = self.line.split(" ")
        decode_space = []
        joined = False
        for i in range(len(splited)):
            if len(splited[i]) > 0:
                if splited[i][0] == "\"":
                    joined = True
                    decode_space.append("".join(splited[i][1:]))
                    continue
                if splited[i][-1] == "\"":
                    joined = False
                    decode_space[-1] = " ".join([decode_space[-1], "".join(splited[i][0:-1])])
                    continue
                if joined:
                    decode_space[-1] = " ".join([decode_space[-1], "".join(splited[i][0:])])
                    continue
                decode_space.append(splited[i])
        if len(sub) == 0:
            return decode_space
        finish = []
        for i in range(len(sub)//2):
            open_bracket = sub[2*i]
            close_bracket = sub[2*i+1]
            if i == 0:
                for i in decode_space[0:self.line[0:open_bracket].count(" ")]:
                    finish.append(i)
                finish.append(Line(self.line[open_bracket+1:close_bracket]))
            else:
                close_last_bracket = sub[2*i-1]
                for i in decode_space[close_last_bracket:self.line[close_last_bracket:open_bracket].count(" ")]:
                    finish.append(i)
                finish.append(Line(self.line[open_bracket+1:close_bracket]))
        return finish

    def execute(self, global_variable, global_class):
        execution = []
        for i in self.decoded_line:
            if isinstance(i, Line):
                execution.append(str(i.execute(global_variable, global_class)))
            else:
                execution.append(str(i))
        if len("".join(execution)) > 0:
            if "".join(execution[0][:2]) == "//":
                return
            return global_variable[execution[0]].load_command(*execution[1:])
