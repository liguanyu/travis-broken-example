<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>form</title>
</head>
<body>
李冠宇
曹慎
陈典章
一个同学
<br>
Welcome to Software Development!
<br>
<a href="http://23.106.130.178:8000/">Server Monitor</a>
<br>
<form action="" method="post" name="form1">
  <table width="500" border="0" cellpadding="0" cellspacing="0">
   <tr>
     <td width="500" height="30">
      <input type="text" name="num1" size="12">
      和
      <input type="text" name="num2" size="12">
      相比谁大？
      请输入整数
      <br>
      <input type="submit" name="submit" value="判断" style="width:50px;height:20px">
     </td>
   </tr>
  </table>
</form>
</body>
</html>



<?php
require "logic.php";


$compare = new CompareTest;
if( $_POST["submit"] == "判断"){       


    $number1 = intval($_POST['num1']);
    $number2 = intval($_POST['num2']);
    
    echo strval($number1). $compare->test($number1,$number2). strval($number2);
    echo "<br >";
}
?>