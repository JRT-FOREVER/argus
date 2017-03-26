<?php
class User
{
  function __construct() {
    //echo "function construct User";
  }

  public function home()
  {
    require(DIR_VIEW . 'login.php');
  }

  public function login()
  {
    if ($_POST['username'] && $_POST['password']) {
      $_SESSION['user'] = $_POST['username'];
      //echo "login";
      header("location: {$_SERVER['PHP_SELF']}");
    }

  }

  public function logout()
  {
    if(isset($_SESSION['user']))
    {

	    unset($_SESSION['user']);
      header("location: {$_SERVER['PHP_SELF']}");
      /*
      echo "logout";

      $url="/index.php";
      echo '<!--<script LANGUAGE="javascript">';
      echo 'location.href="' . $url . "'";
      echo '</script>-->';
      */
    }
  }

  public function status()
  {
    if($_SESSION['user']) {
      return 0;
    } else {
      return 1;
    }
  }

}
?>
