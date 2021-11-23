<?php

/**
 * Line decoder for Lineup
 *
 * @author MisterMine01
 */
class Line {

    public $line;
    public $decoded_line;

    public function __construct($line) {
        $this->line = $this->clean_line($line);
        $this->decoded_line = $this->decode_line();
    }

    private function get_sub_line() {
        $entry_indices = array();
        $close_indices = array();
        foreach (str_split($this->line) as $key => $value) {
            if (($value == "(") || ($value == "{")) {
                $entry_indices[] = array($key, $value);
            } else if (($value == ")") || ($value == "}")) {
                $close_indices[] = array($key, $value);
            }
        }
        $finish = array();
        for ($i = 0; $i < count($entry_indices); $i++) {
            $finish[] = $entry_indices[$i];
            $finish[] = $close_indices[$i];
            if (($i != 0) && ($finish[count($finish) - 3][0] > $finish[count($finish) - 2][0])) {
                array_splice($finish, count($finish) - 3, 2);
            }
        }
        return $finish;
    }

    private function clean_line($line) {
        $array = array();
        foreach (explode(" ", $line) as $value) {
            if ($value != "") {
                $array[] = $value;
            }
        }
        return join(" ", $array);
    }

    protected function decode_line() {
        $sub = $this->get_sub_line();
        $splited = explode(" ", $this->line);
        $decode_space = array();
        $joined = false;
        for ($i = 0; $i < count($splited); $i++) {
            $splited_word = str_split($splited[$i]);
            if (count($splited_word) > 0) {
                if ($splited_word[0] == "\"") {
                    $joined = true;
                    $decode_space[] = $splited[$i];
                    continue;
                }
                if ($splited_word[count($splited_word) - 1] == "\"") {
                    $joined = false;
                    $data = array($decode_space[count($decode_space)-1]);
                    foreach (array_slice($splited_word, 0, count($splited_word) - 1) as $value) {
                        $data[] = $value;
                    }
                    $decode_space[-1] = join(" ", $data);
                    continue;
                }
                if ($joined) {
                    $data = array($decode_space[-1]);
                    $decode_space[-1] = join(" ", array_merge($data, $splited[$i]));
                    continue;
                }
                $decode_space[] = $splited[$i];
            }
        }
        if (count($sub) == 0) {
            return $decode_space;
        }
        $finish = array();
        for ($i = 0; $i < count($sub) / 2; $i++) {
            $open_bracket = $sub[2 * $i];
            $close_bracket = $sub[2 * $i + 1];
            if ($i == 0) {
                foreach (
                array_splice($decode_space,
                        0,
                        substr_count(
                                substr(
                                        $this->line,
                                        0,
                                        $open_bracket[0]
                                ),
                                " "
                        )
                ) as $value) {
                    $finish[] = $value;
                }
                $line_type = 1;
                if ($open_bracket[1] == "(") {
                    $line_type = 0;
                }
                $finish[] = array($line_type, new Line(substr($this->line, $open_bracket[0] + 1, $close_bracket[0] - (1 + $open_bracket[0]))));
            } else {
                $close_last_bracket = $sub[2 * $i - 1];
                foreach (
                array_splice($decode_space,
                        $close_last_bracket[0],
                        substr_count(
                                substr(
                                        $this->line,
                                        $close_last_bracket[0],
                                        $open_bracket[0] - $close_last_bracket[0]
                                ),
                                " "
                        ) - 1
                ) as $value) {
                    $finish[] = $value;
                }
                $line_type = 1;
                if ($open_bracket[1] == "(") {
                    $line_type = 0;
                }
                $finish[] = array($line_type, new Line(substr($this->line, $open_bracket[0] + 1, $close_bracket[0] - (1 + $open_bracket[0]))));
            }

            if ($i == (count($sub) / 2) - 1) {
                foreach (
                array_splice($decode_space,
                        substr_count(
                                substr(
                                        $this->line,
                                        0,
                                        $close_bracket[0]
                                ),
                                " "
                        ) - 1,
                        0
                ) as $value) {
                    $finish[] = $value;
                }
            }
        }
        return $finish;
    }

    public function execute($global_variable, $global_class) {
        $execution = array();
        foreach ($this->decoded_line as $value) {
            if (is_array($value)) {
                if ($value[0] == 0) {
                    $data = ($value[1])->execute($global_variable, $global_class);
                    $execution[] = $data;
                } else {
                    $execution[] = $value[1];
                }
            } else {
                $execution[] = $value;
            }
        }
        if (count($execution) > 0) {
            if (is_string($execution[0])) {
                if (substr($execution[0], 0, 2) == "//") {
                    return;
                }
            } else {
                return ($global_variable[$execution[0]])->load_command($execution[1], array_splice($execution, 2));
            }
        }
    }
}
