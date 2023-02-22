<?php

include(dirname(__FILE__)."/LineUp/interpreter/Interpreter.php");
include(dirname(__FILE__)."/LineUp/module/module_command.php");
include(dirname(__FILE__)."/LineUp/Version.php");

class LineUp extends Interpreter {
    /**
     * Loads modules and calls the Interpreter.
     * 
     * @param string m_dir The directory of modules.
     * @param string lum file with all loaded modules.
     * @param string e_type The type of return you want.
     */
    public function __construct(string $m_dir, string $lum, string $e_type) {
        load_module($m_dir, $lum);
        parent::__construct(decode_modules(), $e_type);
    }
}

$test = new LineUp("../lumodule", "../lumodule/module.lum", "print");
$test->global_variable["l"]->load_command("../script exemple/main_window.lup", array());