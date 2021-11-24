<?php

/**
 * Description of LuModule
 *
 * @author MisterMine01
 */
class LuModule {
    public function __construct() {
    }
    
    public function add_class($name, $class_data) {
        $this->$name = $class_data;
    }
}

class ModuleSystem {
    public function __construct() {
    }
    
    public function add_module($name) {
        $this->$name = new LuModule();
    }
    
    public function add_class($name, $class_name, $class_data) {
        $this->$name->add_class($class_name, $class_data);
    }
}