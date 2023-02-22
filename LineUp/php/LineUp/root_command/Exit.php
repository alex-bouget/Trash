<?php

/* It's a class that allows you to exit the script and return a value */
class ExitUp
{
    /* It's a reference to the interpreter. */
    public $interpreter;

    /* It's a variable that stores the type of exit. */
    public string $e_type;
    
    /**
     * e function.
     * 
     * @param interpreter The interpreter object.
     * @param string e_type The type of return.
     */
    public function __construct(&$interpreter, string $e_type)
    {
        $this->interpreter = $interpreter;
        $this->e_type = $e_type;
    }

    public function load_command(string $command_name, array $parameters)
    {
        if (is_string($command_name)) {
            $ex = array_splice($parameters, 1);
            $com = $this->interpreter->global_variable[$command_name]->load_command($parameters[0], $ex);
        } else {
            $com = $command_name->load_command($parameters[0], array_splice($parameters, 1));
        }
        if ($this->e_type == "print") {
            var_dump($com);
        } else {
            return array("/L_e*/", $com);
        }
    }
}
