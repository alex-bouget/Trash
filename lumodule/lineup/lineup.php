<?php

class EasyVar extends Execution {
    public $type;
    public $value;


    public function __construct($typer) {
        parent::__construct();
        $this->type = $typer;
        $this->value = null;
    }
}

class IntL extends EasyVar {
    public function __construct() {
        parent::__construct("intval");
    }
}

class FloatL extends EasyVar {	
    public function __construct() {
        parent::__construct("floatval");
    }
}

class StringL extends EasyVar {
	public function __construct() {
		parent::__construct("strval");
	}
	
	public function count($parameters) {
		if (count($parameters) >= 1) {
			return count($parameters[0]);
		} else {
			return count($this->value);
		}
	}
	
	public function linecut($parameters) {
		global $module;
		return $module->lineup->ListL(explode(PHP_EOF, $parameters[0]));
	}
	
	public function fresh($parameters) {
		global $module;
		return $module->lineup->ListL(str_split($parameters[0], $parameters[1]));
	}
}

/*
class Operation(Exec):
    def __init__(self):
        super(Operation, self).__init__()
        self.command = {
            "+": self.plus,
            "-": self.moins,
            "*": self.multi,
            "/": self.divide,
            "//": self.dividei,
            "**": self.exp,
            "%": self.modulo
        }

    def plus(self, n1, n2):
        return n1 + n2

    def moins(self, n1, n2):
        return n1 - n2

    def multi(self, n1, n2):
        return n1 * n2

    def divide(self, n1, n2):
        return n1 / n2

    def dividei(self, n1, n2):
        return n1 // n2

    def exp(self, n1, n2):
        return n1 ** n2

    def modulo(self, n1, n2):
        return n1 % n2


class Condition(Exec):
    def __init__(self):
        super(Condition, self).__init__()
        self.command = {
            "=": self.equal,
            ">=": self.much_equal,
            "<=": self.low_equal,
            "!=": self.not_equal
        }

    def equal(self, n1, n2):
        return n1 == n2

    def much_equal(self, n1, n2):
        return n1 >= n2

    def low_equal(self, n1, n2):
        return n1 <= n2

    def not_equal(self, n1, n2):
        return n1 != n2


class Process(Exec):
    def __init__(self, global_variable, global_class):
        super(Process, self).__init__()
        self.global_variable = global_variable
        self.global_class = global_class
        self.command = {
            "if": self.if_pro,
            "while": self.while_pro,
            "multiple": self.multiple
        }

    def if_pro(self, *args):
        # {} {} {}
        if args[0].execute(self.global_variable, self.global_class):
            return args[1].execute(self.global_variable, self.global_class)
        else:
            if len(args) == 3:
                return args[2].execute(self.global_variable, self.global_class)
        return None

    def multiple(self, *args):
        if isinstance(args[0], str):
            data = []
            for i in args[1].decoded_line:
                data.append(i[1].execute(self.global_variable, self.global_class))
            return data[int(args[0])]
        return [i[1].execute(self.global_variable, self.global_class) for i in args[0].decoded_line]

    def while_pro(self, *arg):
        print("no")


class ListL(Exec):
    def __init__(self, *args):
        super(List, self).__init__()
        self.list = [i for i in args]
        self.command = {
            "get": self.get,
            "set": self.set,
            "setnew": self.setnew,
            "display": self.display
        }

    def get(self, index, lister=None):
        if lister is None:
            return self.list[int(index)]
        else:
            return lister.get(index)

    def set(self, new):
        self.list.append(new)

    def setnew(self, new):
        if isinstance(new, list):
            self.list = new
        else:
            self.list = new.list

    def display(self):
        return "[" + ", ".join([str(i) for i in self.list]) + "]"
		*/