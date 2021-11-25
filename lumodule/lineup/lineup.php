<?php

class EasyVar extends Execution {
    public $type;
    public $value;


    public function __construct($typer) {
        parent::__construct();
        $this->type = $typer;
        $this->value = null;
    }
	
	public function set($parameters) {
		return $this->value;
	}
	
	public function get($parameters) {
		$this->value = $this->type($parameters[0]);
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
		var_dump($parameters);
		return new $module->lineup->ListL(str_split($parameters[0], $parameters[1]));
	}
}

class Operation extends Execution {
	public function __construct() {
		parent::__construct();
	}
	
	public function plus($parameters) {
		return $parameters[0] + $parameters[1];
	}
	
	public function minus($parameters) {
		return $parameters[0] - $parameters[1];
	}
	
	public function multi($parameters) {
		return $parameters[0] * $parameters[1];
	}
	
	public function divide($parameters) {
		return $parameters[0] / $parameters[1];
	}
	
	public function divideFloat($parameters) {
		return floatval($parameters[0]) / $parameters[1];
	}
	
	public function exp($parameters) {
		return $parameters[0] ** $parameters[1];
	}
	
	public function modulo($parameters) {
		return $parameters[0] % $parameters[1];
	}
}

class Condition extends Execution {
	public function __construct() {
		parent::__construct();
	}
	
	public function equal($parameters) {
		return ($parameters[0] == $parameters[1]);
	}
	
	public function Iequal($parameters) {
		return ($parameters[0] >= $parameters[1]);
	}
	
	public function equalI($parameters) {
		return ($parameters[0] <= $parameters[1]);
	}
	
	public function Nequal($parameters) {
		return ($parameters[0] != $parameters[1]);
	}
}

class ListL extends Execution {	
	public $listing;
	
	public function __construct() {
		parent::__construct();
		$this->listing = array();
	}
	
	public function get($parameters) {
		if (isset($parameters[1])) {
			return $parameters[1]->get(array($parameters[0]));
		} else {
			return $this->listing[$parameters[0]];
		}
	}
	
	public function set($parameters) {
		$this->listing[] = $parameters[0];
	}
	
	public function setnew($parameters) {
		return;
	}
	
	public function display($parameters) {
        return "[".implode(", ", $this->listing)."]";
		
	} 
}
/*


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


    def setnew(self, new):
        if isinstance(new, list):
            self.list = new
        else:
            self.list = new.list
		*/