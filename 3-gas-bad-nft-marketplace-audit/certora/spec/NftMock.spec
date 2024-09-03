using NftMock as nft;

methods {
    function totalSupply() external returns uint256 envfree;
    function mint() external; 
    function balanceOf(address) external returns uint256 envfree;
}

rule mintingMintsOneNFT() {
    //arange
    env e;
    address minter;
    require(e.msg.value == 0);
    require(e.msg.sender == minter);

    mathint balanceBefore =  nft.balanceOf(minter);
    //act
    currentContract.mint(e);
    //assert
    assert(to_mathint(nft.balanceOf(minter)) == balanceBefore + 1, "Should be able to mint only one");
}

rule totalSupplyDoesntChange(method f) {
    uint256 totalSupply = nft.totalSupply();

    env e;
    calldataarg arg;

    f(e, arg);

    assert(nft.totalSupply() == totalSupply);
}
// invariant totalSupplyIsNotNegative()
//     totalSupply() >= 0;
