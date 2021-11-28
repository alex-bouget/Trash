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
	
	public function descript($parameters) {
		$data = $this->type;
		return $data($parameters[0]);
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
	/*
	def setnew(self, new):
        if isinstance(new, list):
            self.list = new
        else:
            self.list = new.list
			*/
	
	public function display($parameters) {
        return "[".implode(", ", $this->listing)."]";
		
	} 
}


class Process extends Execution {
	public $global_variable;
	public $global_class;
	
	public function __construct(&$global_variable, &$global_class) {
		$this->global_variable = &$global_variable;
		$this->global_class = &$global_class;
	}
	
	public function if($parameters) {
		if ($parameters[0]->execute($this->global_variable, $this->global_class)) {
			return $parameters[1]->execute($this->global_variable, $this->global_class);
		} else {
			if (count($parameters) == 3) {
				return $parameters[2]->execute($this->global_variable, $this->global_class);
			}
		}
		return null;
	}
	
	public function multiple($parameters) {
		$data = array();
		if (is_string($parameters[0])) {
			$t = null;
			foreach ($parameters[1]->decoded_line as $value) {
				$data[] = $value[1]->execute($this->global_variable, $this->global_class);
			}
			return $data[$t];
		}
		foreach ($parameters[0]->decoded_line as $value) {
			$data[] = $value[1]->execute($this->global_variable, $this->global_class);
		}
		return $data;
	}
}

/*

    def multiple(self, *args):
        if isinstance(args[0], str):
            data = []
            for i in args[1].decoded_line:
                data.append(i[1].execute(self.global_variable, self.global_class))
            return data[int(args[0])]
        return [i[1].execute(self.global_variable, self.global_class) for i in args[0].decoded_line]

    def while_pro(self, *arg):
        print("no")


    
		*/