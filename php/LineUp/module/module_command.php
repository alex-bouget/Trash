<?php
include(dirname(__FILE__)."/exec.php");
include(dirname(__FILE__)."/LuModule.php");
include(dirname(__FILE__)."/../Version.php");


/* 
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Scripting/EmptyPHP.php to edit this template
 */

$module = new ModuleSystem();

function load_module($module_folder, $file) {
    global $module, $modules_version;
    foreach (json_decode(file_get_contents($file), true) as $folder) {
        if (is_dir($module_folder."/".$folder)) {
            $mod = json_decode(file_get_contents($module_folder."/".$folder."/packages.json"), true);
            $module_can = false;
            foreach ($mod["packages-id"]["interpreter-version"] as $version) {
                if (in_array($version, $modules_version)) {
                    $module_can = true;
                    break;
                }
            }
            if ($module_can) {
                $module->add_module($mod["packages-name"]);
                include($module_folder."/".$folder."/".$mod["php-files"]["file"]);
                foreach ($mod["php-files"]["class-name"] as $class_name) {
                    $module->add_class($mod["packages-name"], $class_name, new $class_name());
                }
            }
        }
    }
}

function decode_modules() {
    global $module;
    $data = array();
    foreach ($module as $module_name => $module_data) {
        foreach ($module_data as $class_name => $class_data) {
            $data[$module_name."-".$class_name] = $class_data;
        }
    } 
    return $data;
}