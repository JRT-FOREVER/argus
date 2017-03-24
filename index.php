<?php
define('DIR_CONTROLLER', './app/controller/');
define('DIR_MODEL', './app/model/');
define('DIR_VIEW', './app/view/');
define('DIR_LANGUAGE', './app/language/');

define('DB_PREFIX', 'argus_');

//require('db.php');
session_start();

$hostdir = DIR_CONTROLLER;

$filesnames = scandir($hostdir);

//获取也就是扫描文件夹内的文件及文件夹名存入数组 $filesnames

//default route
if (!isset($_GET['class'])) {
  $_GET['class'] = 'home';
}

//var_dump($_GET);
$class_name = $_GET['class'];

foreach ($filesnames as $file_name) {
  //echo $file_name;
  //echo "<br/>";
  if ($file_name == $class_name . '.php') {

    require(DIR_CONTROLLER . $file_name);

    $object = new $class_name;

    $method = $_GET['method'];
    //$object->logout();
    //echo $method;
    $object->$method();

  } else {
    //echo "not found class";
  }
}

/*
$user_name = "sssdd";
$telephone = "sss";

$sql = "INSERT INTO " . DB_PREFIX . "users SET user_name = '" . $user_name . "'";
//echo $sql;
$res = $db->query($sql);
if($res){
    //echo "success";
}
*/

require(DIR_CONTROLLER . 'home.php');
?>
