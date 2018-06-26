<?php
require "logic.php";

class Test extends PHPUnit_Framework_TestCase
{

	public function testTenPlusTen() {
		$compare = new CompareTest;
		$this->assertEquals($compare->test(10,10),"=");
		$this->assertEquals($compare->test(11,10),">");
		$this->assertEquals($compare->test(10,11),"<");
  	}
}

?>
