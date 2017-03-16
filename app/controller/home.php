<?php
require(DIR_LANGUAGE . 'text.php');

require(DIR_MODEL . 'exec.php');


require('user.php');
//user();
$name = $_POST['fname'];
if(user($name)) {

  $exe = new Exec;
  if ($exe->add('key') == 0) {
    $message = $name;
  } else {
    $message = "error";
  }

} else {
  $message = "error";
}

require(DIR_VIEW . 'page.php');
?>
