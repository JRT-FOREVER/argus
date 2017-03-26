<?php
require(DIR_LANGUAGE . 'text.php');

require(DIR_MODEL . 'exec.php');


require('user.php');
require(DIR_CONTROLLER . 'user.php');

//var_dump($_SESSION);
$user = new user();
//user();
//var_dump($_POST);



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
