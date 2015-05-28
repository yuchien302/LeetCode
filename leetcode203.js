function ListNode(val) {
    this.val = val;
    this.next = null;
}
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function(head, val) {
	if(head === null)
		return null;

	var prev = head;
	var temp = prev.next;


	while(prev.val === val) {
		prev = temp;
		if(prev === null)
			return null;
		temp = temp.next;
	}
	var newHead = prev;

	while(temp) {

		if(temp.val === val) {
			prev.next = temp.next;
			temp = temp.next;
		} else {
			prev = temp;
			temp = temp.next;
		}

	}
	return newHead;
    
};

var n1 = new ListNode(1)
// var n2 = new ListNode(2)
// var n3 = new ListNode(3)
// var n4 = new ListNode(4)
// var n5 = new ListNode(5)
// n1.next = n2;
// n2.next = n3;
// n3.next = n4;
// n4.next = n5;
// 
n1 = removeElements(n1, 1)

console.log(JSON.stringify(n1, undefined, 10))
console.log("done.")
process.exit()