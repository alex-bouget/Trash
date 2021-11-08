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
                for x in decode_space[0:self.line[0:open_bracket].count(" ")]:
                    finish.append(x)
                finish.append(Line(self.line[open_bracket+1:close_bracket]))
            else:
                close_last_bracket = sub[2*i-1]
                for x in decode_space[close_last_bracket:self.line[close_last_bracket:open_bracket].count(" ")]:
                    finish.append(x)
                finish.append(Line(self.line[open_bracket+1:close_bracket]))
        return finish

    def execute(self, global_variable, global_class):
        execution = []
        is_instance_command = False
        print(self.decoded_line)
        for i in self.decoded_line:
            if isinstance(i, Line):
                data = i.execute(global_variable, global_class)
                if len(execution) == 0 and type(data) is str:
                    is_instance_command = True
                execution.append(data)
            else:
                execution.append(i)
        try:
            if "".join(execution[0][:2]) == "//":
                return
        except IndexError:
            return
        print(execution)
        if is_instance_command:
            return execution[0].load_command(*execution[1:])
        return global_variable[execution[0]].load_command(*execution[1:])
