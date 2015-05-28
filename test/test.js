var assert = require("assert")
var leetcode202 = require("../leetcode202")
var leetcode191 = require("../leetcode191")


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