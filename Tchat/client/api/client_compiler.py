import json
class compiler:
    def __init__(self, json_data):
        self.data = json.loads(json_data)
    def type_function(self, api_ask, function_data, name):
        data = []
        wait = []
        wait.append("def "+name+"(self")
        try:
            for params in function_data["value"]:
                wait.append(","+params)
        except KeyError:
            pass
        wait.append("):")
        data.append("".join(wait))
        wait = []
        wait.append("    get = self.connect(")
        try:
            for i in api_ask:
                wait.append(i+"='"+api_ask[i]+"'")
        except KeyError:
            pass
        try:
            for i in function_data["ask"]:
                wait.append(","+i+"='"+function_data["ask"][i]+"'")
        except KeyError:
            pass
        try:
            for i in function_data["value"]:
                wait.append(","+i+"="+i)
        except KeyError:
            pass
        wait.append(")")
        data.append("".join(wait))
        data.append("    try:")
        data.append("        get['error']")
        data.append("        raise OSError(get['error'])")
        data.append("    except KeyError:")
        data.append("        "+function_data["python_return"])
        ret = []
        for ui in data:
            ret.append("    "+ui)
        return "\n".join(ret)
    def compile(self, python_file):
        Api= []
        load_class = []
        for class_api in self.data:
            Api.append("class "+class_api+"(api.API):")
            Api.append("    def __init__(self,adress):")
            Api.append("        api.API.__init__(self, adress)")
            for func in self.data[class_api]:
                if func!="ask" and func!="php" and func!="name_function":
                    Api.append(self.type_function(self.data[class_api]["ask"], self.data[class_api][func], func))
            load_class.append("        self."+self.data[class_api]["name_function"]+"="+class_api+"(adress)")
        Api.append("class App_Api():")
        Api.append("    def __init__(self, adress):")
        Api.append("\n".join(load_class))
        open(python_file, "w").write("\n".join(Api))