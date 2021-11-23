<?php
/**
 * Description of Exit
 *
 * @author Administrator
 */
class ExitUp {
    public $interpreter;
    public $e_type;

    public function __construct($interpreter, $e_type) {
        $this->interpreter = $interpreter;
        $this->e_type = $e_type;
    }
    
    public function load_command($command_name, $parameters) {
        if (is_string($command_name)) {
            $com = $this->interpreter->global_variable[$command_name]->load_command($parameters);
        } else {
            $com = $command_name->load_command($parameters[0], array_splice($parameters, 1));
        }
        if ($this->e_type == "print") {
            print($com);
        } else {
            return array("/L_e*/", $com);
        }
    }
}
