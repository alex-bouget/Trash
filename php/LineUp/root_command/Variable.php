<?php

/**
 * Description of Variable
 *
 * @author Administrator
 */
class Variable {

    //put your code here
    public $interpreter;

    public function __construct($interpreter) {
        $this->interpreter = $interpreter;
    }

    public function load_command($command_name, $name, $global = "") {
        if ($globale == "global") {
            $this->interpreter->global_variable[command_name] =
                    new $this->interpreter->global_class[name]($this->interpreter->global_variable,
                            $this->interpreter->global_class);
        } else {
            $this->interpreter->global_variable[command_name] =
                    new $this->interpreter->global_class[name]();
        }
    }
}
