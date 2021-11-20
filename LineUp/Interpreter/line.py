class Line:
    def __init__(self, line):
        self.line = self.clean_line(line)
        self.comment = False
        self.decoded_line = self.decode_line()

    def get_sub_line(self):
        entry_indices = [[i, x] for i, x in enumerate(self.line) if x == "(" or x == "{"]
        close_indices = [[i, x] for i, x in enumerate(self.line) if x == ")" or x == "}"]

        finish = []
        for i in range(len(entry_indices)):
            finish.append(entry_indices[i])
            finish.append(close_indices[i])
            if i != 0 and finish[-3][0] > finish[-2][0]:
                del finish[-2]
                del finish[-2]
        return finish

    def clean_line(self, line):
        return " ".join([i for i in line.split(" ") if i != ""])

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
                for x in decode_space[0:self.line[0:open_bracket[0]].count(" ")]:
                    finish.append(x)
                finish.append([0 if open_bracket[1] == "(" else 1,
                               Line(self.line[open_bracket[0]+1:close_bracket[0]])])
            else:
                close_last_bracket = sub[2*i-1]
                for x in decode_space[close_last_bracket[0]:self.line[close_last_bracket[0]:open_bracket[0]].count(" ")]:
                    finish.append(x)
                finish.append([0 if open_bracket[1] == "(" else 1,
                               Line(self.line[open_bracket[0]+1:close_bracket[0]])])
            if i == (len(sub)//2)-1:
                for x in decode_space[self.line[0:close_bracket[0]].count(" ")+1:self.line[0:-1].count(" ")+1]:
                    finish.append(x)
        return finish

    def execute(self, global_variable, global_class):
        execution = []
        for i in self.decoded_line:
            if isinstance(i, list):
                if i[0] == 0:
                    data = i[1].execute(global_variable, global_class)
                    execution.append(data)
                else:
                    execution.append(i[1])
            else:
                execution.append(i)
        try:
            if "".join(execution[0][:2]) == "//":
                return
        except IndexError:
            return
        return global_variable[execution[0]].load_command(*execution[1:])
