contract Wallet{
    uint256 balance;
    function checkAndPay(bytes32 sol,address dest,uint amt){
        //当余额不足的时候发送将会失败，从而没有奖励
        balance -= amt;
        if(solution != correct){
            throw;
        }
        dest.send(amt);
    }
}
contract AttackerContract{
    function(){
        for(uint i=0; i < investtors.length; i++){
            if(investors[i].invested == min_investment){
                payout = investors[i].payout;
                if(!(investors[i].address.send(payout))){
                    throw;
                }
                investors[i] = newInvestor;
            }
        }
    }
}