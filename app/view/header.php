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
