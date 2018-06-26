<?php
class CompareTest
{
    # 0 1 2
	# < = >
    public function test($num1, $num2) {
        if($num1>$num2){
            return ">";
        }elseif($num1<$num2){
            return "<";
        }else{
            return "=";
        }
    }
}
?>