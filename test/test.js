var assert = require("assert")
var leetcode202 = require("../leetcode202")
var leetcode191 = require("../leetcode191")
var leetcode217 = require("../leetcode217");
var leetcode219 = require("../Leetcode219");


describe('Leetcode219', function(){
  describe('#containsNearbyDuplicate()', function(){
    it('should return false:  ', function(){
      assert.equal(leetcode219.containsNearbyDuplicate([1, 2, 3, 5, 1], 1), false);
      // assert.equal(leetcode219.containsNearbyDuplicate([2, 1, 3], 2), false);
      // assert.equal(leetcode219.containsNearbyDuplicate([]), false);
    });
    it('should return true: [1, 2, 3, 1]', function(){
      assert.equal(leetcode219.containsNearbyDuplicate([1, 2, 3, 1], 4), true);
    });
    it('should return true: [2, 2]', function(){
      assert.equal(leetcode219.containsNearbyDuplicate([2, 2], 1), true);
    });
  });
});



describe('Leetcode217', function(){
  describe('#containsDuplicate()', function(){
    it('should return false:  ', function(){
      assert.equal(leetcode217.containsDuplicate([1, 2, 3, 5, 7]), false);
      assert.equal(leetcode217.containsDuplicate([2, 1, 3]), false);
      assert.equal(leetcode217.containsDuplicate([]), false);
    });
    it('should return true: [1, 2, 3, 1]', function(){
      assert.equal(leetcode217.containsDuplicate([1, 2, 3, 1]), true);
    });
    it('should return true: [2, 2]', function(){
      assert.equal(leetcode217.containsDuplicate([2, 2]), true);
    });
  });
});

describe('Leetcode191', function(){
  describe('#hammingWeight()', function(){
    it('should return false: num < 0 ', function(){
      assert.equal(false, leetcode191.hammingWeight(-10));
      assert.equal(false, leetcode191.hammingWeight(-1));
    })
    it('should equal 3: 7, 11, 22', function(){
      assert.equal(3, leetcode191.hammingWeight(7));
      assert.equal(3, leetcode191.hammingWeight(11));
      assert.equal(3, leetcode191.hammingWeight(22));
    })
    it('should equal 1: 2147483648, 2', function(){
      assert.equal(1, leetcode191.hammingWeight(2147483648));
      assert.equal(1, leetcode191.hammingWeight(2));
    })
  })
 
})


describe('Leetcode202', function(){
  describe('#isHappy()', function(){
    it('should return false: num < 0 ', function(){
      assert.equal(false, leetcode202.isHappy(-10));
      assert.equal(false, leetcode202.isHappy(-1));
    })
	it('should return false: num = 89', function(){
      assert.equal(false, leetcode202.isHappy(89));
    })
    it('should return true: num = 1, 19, 10', function(){
      assert.equal(true, leetcode202.isHappy(1));
      assert.equal(true, leetcode202.isHappy(10));
      assert.equal(true, leetcode202.isHappy(19));
    })
  })
  describe('#next()', function(){
    it('should equal 145: 89', function(){
      assert.equal(145, leetcode202.next(89));
    })
	it('should equal 1: 1, 10', function(){
      assert.equal(1, leetcode202.next(1));
      assert.equal(1, leetcode202.next(10));
    })

  })  
})