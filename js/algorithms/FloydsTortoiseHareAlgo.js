
/**
 * This function implements an algorithm called floyd's
    tortoise and hare algorithm. It can be used to find whether
    or not a cycle exists in a linked list, and at which node
    the cycle starts at using O(1) space (versus doing the above
    tasks with a hash-set or Hash Map).

 * @param {object} node Head of linked list
 * @param {number} node.val Value at current node in linked list
 * @param {object} node.next Next node in the linked list
 * @returns {(object|null)} Node that starts the linked list or null if there is no cycle in the linked list
 */
function floydsTortoiseHareAlgo(node) {
   if (node == null || node.next == null) {
       return null;
   }
   let ptr1 = node;
   let ptr2 = node; 
   while (ptr2 && ptr2.next) {
       ptr1 = ptr1.next;
       ptr2 = ptr2.next.next;
       if (ptr1 === ptr2) {
           break;
       }
   }
   if (ptr1 !== ptr2) {
       return null; 
   }
   ptr1 = node;
   while (ptr1 !== ptr2) {
       ptr1 = ptr1.next;
       ptr2 = ptr2.next; 
   }
   return ptr1; 
}


export {floydsTortoiseHareAlgo}; 