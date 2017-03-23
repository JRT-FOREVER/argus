<?php

define('DIR_CONTROLLER', './app/controller/');
define('DIR_MODEL', './app/model/');
define('DIR_VIEW', './app/view/');
define('DIR_LANGUAGE', './app/language/');



define('DB_PREFIX', 'argus_');

require('db.php');


$hostdir = DIR_CONTROLLER;

  $filesnames = scandir($hostdir);

//获取也就是扫描文件夹内的文件及文件夹名存入数组 $filesnames

var_dump($_GET);

foreach ($filesnames as $name) {
  //$name = substr($name , '.');
  echo $name;
  echo "<br/>";
  if ($name == $_GET['class']) {
    echo "66666";
    require(DIR_CONTROLLER . $name .'.php');

    $class = new $name;
    $class->$_GET['method'];
  } else {
    //echo "not found class";
  }


}






$user_name = "sssdd";
$telephone = "sss";

$sql = "INSERT INTO " . DB_PREFIX . "users SET user_name = '" . $user_name . "'";
//echo $sql;
$res = $db->query($sql);
if($res){
    //echo "success";
}




require(DIR_CONTROLLER . 'home.php');

?>
