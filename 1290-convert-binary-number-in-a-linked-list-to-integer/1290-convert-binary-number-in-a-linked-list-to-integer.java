/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int getDecimalValue(ListNode head) {
        ListNode temp=head;
        int count=0;
        int num=0;
        while(temp.next!=null){
            count++;
            temp=temp.next;
        }
        temp=head;
        while(count>=0){
            num+=temp.val*Math.pow(2,count);
            temp=temp.next;
            count--;
        }
       return num; 
    }
}