
using GasBadNftMarketplace as gasBadNftMarketplace;
using NftMarketplace as nftMarketplace;

methods {
    function _.safeTransferFrom(address,address,uint256) external => DISPATCHER(true);
    function _.onERC721Received(address,address,uint256,bytes) external => DISPATCHER(true);
    function getListing(address nftAddress, uint256 tokenId) external returns (INftMarketplace.Listing) envfree;
    function getProceeds(address seller) external returns (uint256) envfree;
}

ghost mathint listingUpdatesCount {
    init_state axiom listingUpdatesCount == 0;
}

ghost mathint log4Count {
    init_state axiom log4Count == 0;
}


hook Sstore s_listings[KEY address nftAddress][KEY uint256 tokenId].price uint256 cow {
    listingUpdatesCount = listingUpdatesCount + 1;
}

hook LOG4(uint offset, uint length, bytes32 t1, bytes32 t2, bytes32 t3, bytes32 t4) uint256 logging {
    log4Count = log4Count + 1;
}  


invariant anytime_mapping_updated_emit_event()
    listingUpdatesCount <= log4Count;

rule calling_any_function_should_result_in_each_contract_having_the_same_state(method f, method f2) {
    env e;
    calldataarg args;
    address seller;
    address nftAddress;
    uint256 tokenId;

    require(f.selector == f2.selector);

    require(gasBadNftMarketplace.getProceeds(e, seller) == nftMarketplace.getProceeds(e, seller));
    require(gasBadNftMarketplace.getListing(e, nftAddress, tokenId).price == nftMarketplace.getListing(e, nftAddress, tokenId).price);
    require(gasBadNftMarketplace.getListing(e, nftAddress, tokenId).seller == nftMarketplace.getListing(e, nftAddress, tokenId).seller);

    gasBadNftMarketplace.f(e, args); 
    nftMarketplace.f2(e, args);
 
    assert(gasBadNftMarketplace.getProceeds(e, seller) == nftMarketplace.getProceeds(e, seller));
    assert(gasBadNftMarketplace.getListing(e, nftAddress, tokenId).price == nftMarketplace.getListing(e, nftAddress, tokenId).price);
    assert(gasBadNftMarketplace.getListing(e, nftAddress, tokenId).seller == nftMarketplace.getListing(e, nftAddress, tokenId).seller);
}