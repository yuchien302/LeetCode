/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
	var tab = {};
    for(var i=0; i<nums.length; i++){
    	if(tab[nums[i]]!==undefined && (i-tab[nums[i]]) <= k ){
    		return true;
    	} else {
            tab[nums[i]] = i;
    	}
    }
    return false;
};

module.exports = { 
	containsNearbyDuplicate: containsNearbyDuplicate
};