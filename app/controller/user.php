<?php
class User
{
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
    echo "6666666666666";
    if(isset($_SESSION['user']))
    {
	     unset($_SESSION['user']);
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
