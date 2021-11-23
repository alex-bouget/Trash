<?php
include "Line.php";

/**
 * Description of Interpreter
 *
 * @author MisterMine01
 */
class Interpreter {
    public $global_variable;
    public $global_class;
    
    public function __construct($module, $e_string) {
        $this->global_variable = array();
        $this->global_class = $module;
    }
    
    public function set_class($name, $value) {
        $this->global_class[$name] = $value;
    }
    
    public function execute($file) {
        foreach (explode(";", file_get_contents($file)) as $value) {
            $data = new Line($value);
            if (is_array($data) && $data[0] == "/L_e*/") {
                return $data[1];
            }
        }
    }
}
