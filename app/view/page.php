<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title><?php echo $text_title;?></title>
  <script src="public/components/jquery/dist/jquery.min.js" type="text/javascript"></script>
  <link href="public/components/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet" media="screen" />
  <script src="public/components/bootstrap/dist/js/bootstrap.min.js" type="text/javascript"></script>
</head>
<body>
<header>
  <div class="container">
   <div class="text-center">
    <div class="visible-xs">
    <?php echo $text_today . date("Y-m-d  l") . "<br>"; ?>
    </div>
    <img class="img-responsive center-block" src=<?php echo $img_logo; ?> alt="logo" /></div>
   </div>
  </div>
</header>
<div class="container text-center">
  <div class="col-sm-6">
   <img class="img-responsive center-block" src=<?php echo $img_main; ?> alt="main" />
  </div>
 <div class="col-sm-6">
  <div class="hidden-xs">
   <?php echo $text_today . date("Y-m-d  l") . "<br>"; ?>
  </div>
  <?php if ($user->status()) {
    $user->home();
  } else { ?>
    <div>hello <?php echo $_SESSION['user']; ?>
    <a href="<?php echo $_SERVER['PHP_SELF']; ?>?class=user&method=logout"><?php echo $text_logout; ?></a></div>
  <form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
    <br />
    KEY: <input type="text" name="fname">
    <input type="submit" value="Start">
  </form>
  <?php } ?>
  <?php echo $message ?>
   	<div class="text-center">
   	  <a href="./elFinder-2.x/elfinder.html">帮助</a>-<a href="http://59.72.114.29">首页</a>
   	  <hr>
   	  <div><?php echo $text_footer;?></div>
   	</div>
  </div>
</div>
<footer>
  <div class="container text-center">
  </div>
</footer>
</body></html>
