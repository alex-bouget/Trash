<?php

/**
 * Description of Variable
 *
 * @author Administrator
 */
class Variable {

    //put your code here
    public $interpreter;

    public function __construct(&$interpreter) {
        $this->interpreter = $interpreter;
    }

    public function load_command($command_name, $parameters) {
        if (count($parameters) > 1 && $parameters[1] == "global") {
            $classic = get_class($this->interpreter->global_class[$parameters[0]]);
            $this->interpreter->global_variable[$command_name] =
                    new $classic($this->interpreter->global_variable,
                            $this->interpreter->global_class);
        } else {
            $classic = get_class($this->interpreter->global_class[$parameters[0]]);
            $this->interpreter->global_variable[$command_name] = new $classic();
        }
    }
}
