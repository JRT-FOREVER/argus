<!DOCTYPE html PUBLIC "-//WAPFORUM//DTD XHTML Mobile 1.0//EN" "http://www.wapforum.org/DTD/xhtml-mobile10.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<!--STATUS OK--><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta http-equiv="Cache-control" content="no-cache" />
<style type="text/css">
body{font-size:medium;line-height:1.6em;text-align:center;}
img{border:0;}
form{margin:0;padding:0;}.a{padding-top:6px;margin-top:6px;margin-bottom:6px;}.h{color:rgb(8, 8, 31);}.s{font-size:small;}.b{font-size:small;color:#77C;}
</style>
<title>JRT_key</title>
</head>
<body>
<div>
<span class="h">
<?php
echo "今天是 " . date("Y-m-d  l") . "<br>";
?>
</span>
<img src="JRT_key/JRT_logo.jpg" alt="JRT首页" />
<br />

<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
<br />
KEY: <input type="text" name="fname">
<input type="submit" value="Start" name="ct_2" />
</form>
<?php 
$name = $_POST['fname'];
if($name==="robotteam") { 
	echo $name;
	$myfile = fopen("exec.txt", "w") or die("Unable to open file!");
	$txt = "key";
	fwrite($myfile, $txt);
	fclose($myfile);
//	system('./key.py');
}
else {
	echo "error";
}
?>
<div class="a">
<a href="./elFinder-2.x/elfinder.html">帮助</a>
-
<a href="http://wapp.baidu.com/f?kw=%B0%D9%B6%C8%B8%F6%C8%CB%CA%D7%D2%B3&amp;ssid=0&amp;from=1011267m&amp;bd_page_type=1&amp;uid=0&amp;pu=sz%40224_220%2Cta%40middle____">反馈</a>
<br />
<span class="b">JRT 唐敖庆B512号</span>
</div></div></body></html>
