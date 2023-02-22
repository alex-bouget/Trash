<?php
class Main extends Execution
{
    public $global_variable;
    public $global_class;
    private $graphic;

    public function __construct(&$global_variable, &$global_class)
    {
        $this->global_variable = &$global_variable;
        $this->global_class = &$global_class;
    }

    public function begin($parameters)
    {
        $this->graphic = array("<!DOCTYPE html>", "<html>");
    }

    public function end($parameters)
    {
        $this->graphic[] = "</html>";
    }
    public function view($parameters)
    {
        echo implode("\n", $this->graphic);
    }
    public function text($parameters)
    {
        $this->graphic[] = $parameters[0];
    }
    public function style($parameters)
    {
        $this->graphic[] = "style=\"";
        foreach ($parameters[0]->decoded_line as $value) {
            $this->graphic[] = $value[1]->decoded_line[0].": ".$value[1]->decoded_line[1].";";
        }
        $this->graphic[] = "\"";
    }

    public function win($parameters)
    {
        $this->graphic[] = "<".$parameters[0];
        foreach ($parameters[1]->decoded_line as $value) {
            $value[1]->execute($this->global_variable, $this->global_class);
        }
        $this->graphic[] =  ">";
        if (count($parameters) >= 3) {
            foreach ($parameters[2]->decoded_line as $value) {
                $value[1]->execute($this->global_variable, $this->global_class);
            }
            $this->graphic[] = "</".$parameters[0].">";
        }
    }
}
