<?php

/**
 * Description of command
 *
 * @author MisterMine01
 */
class Execution {
    public $command;

    public function __construct() {
        $this->command = array();
    }
    
    public function load_command($command_name, $parameters) {
        $this->command[$command_name]($parameters);
    }
}
