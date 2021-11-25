<?php

/**
 * Description of command
 *
 * @author MisterMine01
 */
class Execution {

    public function __construct() {
    }
    
    public function load_command($command_name, $parameters) {
        return $this->$command_name($parameters);
    }
}
