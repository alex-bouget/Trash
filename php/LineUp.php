<?php

include(dirname(__FILE__)."/LineUp/interpreter/Interpreter.php");
include(dirname(__FILE__)."/LineUp/module/module_command.php");

/**
 * Description of LineUp
 *
 * @author MisterMine01
 */
class LineUp extends Interpreter {
    public function __construct($m_dir, $lum, $e_type) {
        load_module($m_dir, $lum);
        parent::__construct(decode_modules(), $e_type);
    }
}

$test = new LineUp("../lumodule", "../lumodule/module.lum", "print");
$test->execute("../script exemple/main_window.lup");