<?php
require "logic.php";

class Test extends SumTest
{
	# 0 1 2
	# < = >
	public function testTenPlusTen() {
		$this->assertEquals($this->test(10,10),0);
		$this->assertEquals($this->test(11,10),2);
		$this->assertEquals($this->test(10,11),0);
  	}
}

?>
