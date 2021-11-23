<?php

class EasyVar extends Execution {
    public $type;
    public $value;


    public function __construct($typer) {
        parent::__construct();
        $this->type = $typer;
        $this->value = null;
        $this->command = array(
            "set" => $this->set,
            "get" => $this->get,
            "descript" => $this->descript
        );
    }
    
    public function set($p1) {
        $this->value = $this->type($p1[0]);
    }
    
    public function get() {
        return $this->value;
    }
    public function descript($value) {
        return $this->type($value[0]);
    }
}

class IntL extends EasyVar {
    public function __construct() {
        parent::__construct(intval);
    }
}

class FloatL extends EasyVar {
    public function __construct() {
        parent::__construct(floatval);
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