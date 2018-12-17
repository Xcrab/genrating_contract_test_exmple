pragma solidity ^0.4.23;

contract ChangeValue{
    uint256 public tot = 100;
    
    function add(uint a,uint b) public returns(uint256){
        iadd(a + b);
        return tot;
    }

    function sub(uint a) public returns(uint256){
        isub(a);
        return tot;
    }

    function iadd(uint a) internal{
        tot = tot + a;
    }

    function isub(uint a) internal{
        tot = tot - a;
    }
}