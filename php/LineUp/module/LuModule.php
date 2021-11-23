<?php

/**
 * Description of LuModule
 *
 * @author MisterMine01
 */
class LuModule {
    public $class_data;
    public function __construct() {
        $this->class_data = array();
    }
    
    public function add_class($name, $class_data) {
        $this->$name = $class_data;
        $this->class_data[$name] = $this->$name;
    }
}

class ModuleSystem {
    public $module_name;
    public function __construct() {
        $this->module_name = array();
    }
    
    public function add_module($name) {
        $this->$name = new LuModule;
        $this->module_name = $this->$name;
    }
    
    public function add_class($module_name, $class_name, $class_data) {
        $this->module_name[$name].add_class($class_name, $class_data);
    }
}