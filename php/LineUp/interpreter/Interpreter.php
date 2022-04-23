<?php
include(dirname(__FILE__)."/Line.php");
include(dirname(__FILE__)."/../root_command/Exit.php");
include(dirname(__FILE__)."/../root_command/Variable.php");
include(dirname(__FILE__)."/../root_command/Lup.php");

/**
 * Description of Interpreter
 *
 * @author MisterMine01
 */
class Interpreter {
    public $global_variable;
    public $global_class;
    
    public function __construct($module, $e_string) {
        $this->global_variable = array(
            "v" => new Variable($this),
            "e" => new ExitUp($this, $e_string),
            "l" => new Lup($this)
        );
        $this->global_class = $module;
    }
    
    public function set_class($name, $value) {
        $this->global_class[$name] = $value;
    }
}
