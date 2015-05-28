/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
	var mem = {};
	if(n<=0)
		return false;
	var temp = n;
	while(temp !== 1){
		mem[temp] = true;
		temp = next(temp);
		if(mem[temp] === true){
			return false;
		}
	}
	return true;


};


var next = function(n) {
	var total = 0
	while (n>9) {
		total += Math.pow((n%10), 2);
		n = Math.floor(n/10)
	}
	total += Math.pow(n, 2);
	return total;
}

module.exports = { 
	isHappy: isHappy,
	next: next
}