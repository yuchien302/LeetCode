var hammingWeight = function(n) {
	if(n<0) return 0;
	var max = Math.pow(2, 31);
	var count = 0;
    for (var i = 0; i <= 31 ; i++) {
		if( (n & Math.pow(2, i)) !== 0)
			count++;
    };
    return count;
};

module.exports = { 
	hammingWeight: hammingWeight
}