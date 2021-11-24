<?php

class EasyVar extends Execution {
    public $type;
    public $value;
	public $command;


    public function __construct($typer) {
        parent::__construct();
        $this->type = $typer;
        $this->value = null;
		var_dump($this);
        $this->command = array(
            "set" => function ($p1) {
				$this->value = $this->type($p1[0]);
			},
            "get" => function () {
				return $this->value;
			},
            "descript" => function ($value) {
				return $this->type($value[0]);
			}
        );
    }
}

class IntL extends EasyVar {
    public function __construct() {
        parent::__construct("intval");
    }
}

class FloatL extends EasyVar {
	public $command;
	
    public function __construct() {
        parent::__construct("floatval");
		$this->command = parent::command;
    }
}

    /*
    def __init__(self, args=0):
        super(Int, self).__init__(int)
        self.value = int(args)
}

class Float(EasyVar):
    def __init__(self, args=0):
        super(Float, self).__init__(float)
        self.value = float(args)*/