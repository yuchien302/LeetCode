/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
	var tab = {};
    for(var i=0; i<nums.length; i++){
    	if(!tab[nums[i]]){
    		tab[nums[i]] = true;
    	} else {
    		return true;
    	}
    }
    return false;
};

module.exports = { 
	containsDuplicate: containsDuplicate
};