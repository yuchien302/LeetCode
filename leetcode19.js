
function ListNode(val) {
    this.val = val;
    this.next = null;
}

/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    var total = 1;
    var temp = head;
    while(temp.next){
    	total = total + 1;
    	temp = temp.next;
    }

    // console.log(total)
    var count = total-n-1;
    temp = head;
    // console.log(count)
    while(count > 0){
    	count = count - 1;
    	temp = temp.next;
    }

    if(count === -1)
    	return temp.next;
    else{
    	temp.next = temp.next.next;
    	return head;
    }

    
};

// 1->2->3->4->5, and n = 2.
var n1 = new ListNode(1)
var n2 = new ListNode(2)
var n3 = new ListNode(3)
var n4 = new ListNode(4)
var n5 = new ListNode(5)
n1.next = n2;
n2.next = n3;
n3.next = n4;
n4.next = n5;
n1 = removeNthFromEnd(n1, 2)

// var tempNode = n1;
// tempNode.val = 10;

console.log(JSON.stringify(n1, undefined, 10))
console.log("done.")
process.exit()