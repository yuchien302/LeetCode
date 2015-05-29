
function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
} 

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function(root) {
	if(root===null || isLeaf(root))
		return true;
	else
		return isSymmetric2(root.left, root.right);
	// if (!isLeaf(root.left) && !isLeaf(root.right))
	    
	// else
	// 	return false;
};

var isSymmetric2 = function(tl, tr) {
	// console.log("hi");
	// console.log(tl);
	// console.log(tr);
	if((tl === null) && (tr === null))
		return true;
	else if((tl === null) || (tr === null))
		return false;
	// console.log(tl);
	// console.log(tr);

	if(isLeaf(tl) && isLeaf(tr))
		return tl.val === tr.val;
	else if(!isLeaf(tl) && !isLeaf(tr))
		return (tl.val === tr.val) && isSymmetric2(tl.left, tr.right) && isSymmetric2(tl.right, tr.left);
	else
		return false;

};

var isLeaf = function(node) {
	return (node.left === null) && (node.right === null);
};

var t1 = new TreeNode(2);
// var t2 = new TreeNode(97);
// var t3 = new TreeNode(97);
// var t4 = new TreeNode(47);
// var t5 = new TreeNode(80);
// var t6 = new TreeNode(-7);
// var t7 = new TreeNode(-7);

// t1.left = t2;
t1.right = t2;
// t2.left = t4;
// t2.right = t5;
// t3.left = t6;
// t3.right = t7;


console.log(t1);
console.log(isSymmetric(t1));

process.exit();

[2,97,97,null,47,80,null,-7,null,null,-7]