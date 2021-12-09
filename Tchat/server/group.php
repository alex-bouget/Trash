<?php
function gro_create_group($name_group) {
    if (is_file("group.json")) {
        $Lecture = json_decode(file_get_contents("group.json"), true);
    } else {
        $Lecture = array();
    }
    if (in_array(htmlspecialchars($name_group), $Lecture)) {
        return json_encode(array("error" => "group already created"));
    } else {
        $Lecture[] = $name_group;
        file_put_contents("group.json", json_encode($Lecture));
        file_put_contents("discussion/{$name_group}.json", json_encode(array(array("0", "group created"))));
    }
    return json_encode(array("sending" => "check"));
}
function gro_add_group($name, $group_name) {
    include "accounts.php";
    $Lecture = json_decode(file_get_contents("group.json"), true);
    if (in_array(htmlspecialchars($group_name), $Lecture)) {
        $id = json_decode(acc_get_id_by_name(htmlspecialchars($name)), true)["id"];
        return acc_add_group($id, htmlspecialchars($group_name));
    } else {
        return array("error" => "group not created");
    }
}
function gro_send_in_group($token, $group_name, $msg) {
    $Lecture = json_decode(file_get_contents("discussion/{$group_name}.json"), true);
    $Lecture[] = array(htmlspecialchars($token), htmlspecialchars($msg));
    file_put_contents("discussion/{$group_name}.json", json_encode($Lecture));
    return json_encode(array("sending" => "check"));
}
function gro_get_account($token) {
    include "accounts.php";
    $id = json_decode(acc_get_id_by_token($token), true)["id"];
    return acc_get_all_group($id);
}
function gro_get_in_group($group_name, $lastn) {
    $Lecture = json_decode(file_get_contents("discussion/{$group_name}.json"), true);
    $ret = array();
    include "accounts.php";
    foreach ($Lecture as $key => $value) {
        if ($key >= $lastn) {
            $ret[] = array(json_decode(acc_get_name_by_token($value[0]), true)["name"], $value[1]);
        }
    }
    return json_encode(array("data" => $ret));  
}
?>