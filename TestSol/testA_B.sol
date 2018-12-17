pragma solidity ^0.4.25;

contract A{
    uint256 public tot;
    function A(uint256 _tot){
        tot = _tot;
    }
    function test_1() public returns(uint256){
        return 0;
    }
    function test_2() public returns(uint256){
        return 0;
    }
    function test_3() public returns(uint256){
        return 0;
    }
    function test_4() public returns(uint256){
        return 0;
    }
}

contract B is A{
    function B(uint256 _tot){
        A(_tot);
    }
    function test_5() public returns(uint256){
        return 0;
    }
    function test_6() public returns(uint256){
        return 0;
    }
    function test_7() public returns(uint256){
        return 0;
    }
}