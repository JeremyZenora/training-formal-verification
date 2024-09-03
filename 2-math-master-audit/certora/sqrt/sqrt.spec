
methods {
    function mathMastersSqrt(uint256) external returns (uint256) envfree;
    function sqrtUni(uint256) external returns (uint256) envfree;

    function solmateTopHalf(uint256) external returns (uint256) envfree;
    function mathMastersTopHalf(uint256) external returns (uint256) envfree;
}

 rule compareSolmateTopHalfAndMathMastersTopHalf(uint x) {
    assert(solmateTopHalf(x) == mathMastersTopHalf(x));
 }
