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

  public function login($username, $password)
  {
    $_SESSION['user'] = $_POST['username'];
  }

  public function logout()
  {
    if(isset($_SESSION['user']))
    {

	    unset($_SESSION['user']);

      $url="/index.php";
      echo '<!--<script LANGUAGE="javascript">';
      echo 'location.href="' . $url . "'";
      echo '</script>-->';
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
