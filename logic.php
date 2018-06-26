<?php
class SumTest
{
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