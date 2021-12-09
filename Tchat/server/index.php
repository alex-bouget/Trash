<?php
$data = json_decode(file_get_contents("data.json"),true);
foreach ($data as $value) {
    $test1 = 0;
    foreach ($value["ask"] as $key => $ask) {
        if (isset($_GET[$key])) {
            if (htmlspecialchars($_GET[$key]) == htmlspecialchars($value["ask"][$key])) {
                $test1 = $test1+1;
            }
        }
    }
    if ($test1==count($value["ask"])) {
        include $value["php"];
        $newdata = $value;
        foreach ($newdata as $func => $edfv) {
            if ($func != "ask") {
                if ($func != "php") {
                    if ($func != "name_function") {
                        $test2 = 0;
                        foreach($newdata[$func]["ask"] as $p => $rt) {
                            if (isset($_GET[$p])) {
                                if (htmlspecialchars($_GET[$p]) == $newdata[$func]["ask"][$p]) {
                                    $test2 = $test2+1;
                                }
                            }
                        }
                        if ($test2 == count($newdata[$func]["ask"])) {
                            if (isset($newdata[$func]["value"])) {
                                $yup = array();
                                foreach ($newdata[$func]["value"] as $p) {
                                    if (isset($_GET[$p])) {
                                        $yup[] = htmlspecialchars($_GET[$p]);                               
                                    }
                                }
                                if (count($yup) == count($newdata[$func]["value"])) {
                                    echo $newdata[$func]["php_function"](...$yup);
                                } else {
                                    echo json_encode(array("error"=>"parameters not send"));
                                }
                            } else {
                                echo $newdata[$func]["php_function"]();
                            }
                        }
                    }
                }
            }
        }
    }
}


?>