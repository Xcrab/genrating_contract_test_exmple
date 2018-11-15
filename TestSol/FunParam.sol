pragma solidity ^0.4.23;

contract FunParam{

    function testBool(bool b) public pure returns(bool){
        if(b){
            return true;
        }else{
            return false;
        }
    }

    function testInt(uint8 u8,uint256 u256,int8 i8,int256 i256) public pure returns(int,int){
        int sum = 0;
        if(u8 > 10){
            sum++;
        }
        if(u256 > 10){
            sum++;
        }
        if(i8 > 10){
            sum++;
        }
        if(i256 > 10){
            sum++;
        }
        return (sum,sum*2);
    }

    function testAddress(address ad) public view returns(int){
        if(ad.balance == 0){
            return 0;
        }else{
            return 1;
        }
    }

    function testFixedByte(bytes1 b1,bytes32 b32) public pure returns(bytes32){
        int sum = 0;
        if(b1.length == 0){
            sum++;
        }
        if(b32.length == 0){
            sum++;
        }
        return b32;
    }

    function testUFixedByte(bytes memory b,string memory s) public pure returns(bytes memory,string memory){
        bytes memory bb = b;
        string memory ss = s;
        return (bb,ss);
    }

    function testIntArray(int[10] memory ia,uint[10] memory uia) public pure returns(int){
        int sum = 0;
        if(ia.length < 10){
            sum++;
        }
        if(uia.length < 10){
            sum++;
        }
        return sum;
    }
}