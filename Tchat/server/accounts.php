<?php
function acc_create_accounts($id, $passw, $name) {
    if (is_file("accounts.json")) {
        $Lecture = json_decode(file_get_contents("accounts.json"), true);
    } else {
        $Lecture = array("0" => array("name" => "server", "token"=>"0"));
    }
    if (isset($Lecture[htmlspecialchars($id)]) == false) { #false juste pour mettre les erreur a la fin
        $length = 10;
        $token = substr(str_shuffle(str_repeat($x='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', ceil($length/strlen($x)) )),1,$length);
        $Lecture[htmlspecialchars($id)] = array("name" => htmlspecialchars($name), "password" => htmlspecialchars($passw), "token" => htmlspecialchars($token),"group" => array("general"));
        file_put_contents("accounts.json", json_encode($Lecture));
        return json_encode(array("token"=>htmlspecialchars($token)));
    } else {
        return json_encode(array("error"=>"id already exist"));
    }
}
function acc_connect_accounts($id,$password) {
    $Lecture = json_decode(file_get_contents("accounts.json"), true);
    if (isset($Lecture[htmlspecialchars($id)])) {
        if (htmlspecialchars($Lecture[htmlspecialchars($id)]["password"]) == htmlspecialchars($password)) {
            return json_encode(array("token"=>$Lecture[htmlspecialchars($id)]["token"]));
        } else {
            return json_encode(array("error"=>"wrong password"));
        }
    } else {
        return json_encode(array("error"=>"id not exist"));
    }
}
function acc_all_name() {
    $Lecture = json_decode(file_get_contents("accounts.json"), true);
    $name = array();
    foreach ($lecture as $value) {
        $name[] = $value["name"];
    }
    return json_encode(array("data" => $name));
}



//group function
function acc_add_group($id, $group_name) {
    $Lecture = json_decode(file_get_contents("accounts.json"), true);
    $Lecture[htmlspecialchars($id)]["group"][] = htmlspecialchars($group_name);
    file_put_contents("accounts.json",json_encode($Lecture));
    return json_encode(array("sending" => 'check'));
}
function acc_get_all_group($id) {
    $Lecture = json_decode(file_get_contents("accounts.json"), true);
    return json_encode(array("data" => $Lecture[htmlspecialchars($id)]["group"]));
}


//get function
function acc_get_id_by_token($token) {
    $Lecture = json_decode(file_get_contents("accounts.json"), true);
    foreach ($Lecture as $id => $value) {
        if (htmlspecialchars($token) == htmlspecialchars($value["token"])) {
            $finish = 1;
            return json_encode(array("id" => htmlspecialchars($id)));
            break;
        }
    }
    if (isset($finish) == false) {
        return json_encode(array("error"=>"token not exist"));
    }
}
function acc_get_id_by_name($name) {
    $Lecture = json_decode(file_get_contents("accounts.json"), true);
    foreach ($Lecture as $id => $value) {
        if (htmlspecialchars($name) == htmlspecialchars($value["name"])) {
            $finish = 1;
            return json_encode(array("id" => htmlspecialchars($id)));
            break;
        }
    }
    if (isset($finish) == false) {
        return json_encode(array("error"=>"name not exist"));
    }
}
function acc_get_name_by_token($token) {
    $Lecture = json_decode(file_get_contents("accounts.json"), true);
    foreach ($Lecture as $value) {
        if (htmlspecialchars($token) == htmlspecialchars($value["token"])) {
            $finish = 1;
            return json_encode(array("name" => htmlspecialchars($value["name"])));
            break;
        }
    }
    if (isset($finish) == false) {
        return json_encode(array("error"=>"token not exist"));
    }
}
?>