/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    return isIsomorphic2(s, t) && isIsomorphic2(t, s);
};

var isIsomorphic2 = function(s, t) {
    if((s.length === t.length) && ((s.length === 0) || (s.length === 1))){
    	return true;
    } else if(s.length !== t.length) {
    	return false;
    } else {
    	m = {};
    	for (var i = 0; i < s.length; i++) {
    		if(!m[s[i]]){
    			m[s[i]] = t[i];
    		} else if(m[s[i]] !== t[i]) {
    			return false;
    		}
    	}
    	return true;
    }
};


console.log(isIsomorphic("add", "egg"));
console.log(isIsomorphic("foo", "bar"));
console.log(isIsomorphic("paper", "title"));
console.log(isIsomorphic("ab", "aa"));