pragma solidity ^0.4.23;

contract HelloWorld{
    function show() public pure returns(string){
        return "HelloWorld";
    }
    function add(int a,int b) public pure returns(int){
        return a + b;
    }
    function sub(int a,int b) public pure returns(int){
        if(a > b){
            return a - b;
        }else{
            return b - a;
        }
    }
}
