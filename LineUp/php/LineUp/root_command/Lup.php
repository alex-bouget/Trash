<?php

/* It executes a file. */
class Lup
{
    public $interpreter;

    public function __construct(&$interpreter)
    {
        $this->interpreter = $interpreter;
    }

    public function load_command($command_name, $parameters)
    {
        return $this->execute($command_name);
    }

    private function execute($file)
    {
        foreach (explode(";", file_get_contents($file)) as $value) {
            $data = (new Line(
                    implode(" ", explode(PHP_EOL, $value))
                )
            )->execute(
                $this->interpreter->global_variable,
                $this->interpreter->global_class
            );
            if (is_array($data) && $data[0] == "/L_e*/") {
                return $data[1];
            }
        }
    }
}
