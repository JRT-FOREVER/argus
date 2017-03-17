<?php

define('DIR_CONTROLLER', './app/controller/');
define('DIR_MODEL', './app/model/');
define('DIR_VIEW', './app/view/');
define('DIR_LANGUAGE', './app/language/');



define('DB_PREFIX', 'argus_');

require('db.php');


$user_name = "sssdd";
$telephone = "sss";

$sql = "INSERT INTO " . DB_PREFIX . "users SET user_name = '" . $user_name . "'";
echo $sql;
$res = $db->query($sql);
if($res){
    echo "success";
}




require(DIR_CONTROLLER . 'home.php');

?>
