<?php
class SumTest
{
    # 0 1 2
	# < = >
    public function test($num1, $num2) {
        if($num1>$num2){
            return 2;
        }elseif($num1<$num2){
            return 0;
        }else{
            return 1;
        }
    }
}
?>