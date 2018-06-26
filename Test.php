<?php
require "logic.php";

class Test extends SumTest
{
	public function testTenPlusTen() {
		$this->assertEquals($this->test(10,10),'=');
		$this->assertEquals($this->test(11,10),'>');
		$this->assertEquals($this->test(10,11),'<');
  	}
}

?>
