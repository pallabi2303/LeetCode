/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public static ArrayList<Integer> findLeaf(TreeNode root1,ArrayList<Integer> list1){
        if(root1==null){
            return list1;
        }
        if(root1.left==null & root1.right==null){
            list1.add(root1.val);
        }
    findLeaf(root1.left,list1);
    findLeaf(root1.right,list1);
    return list1;
        
        
        
    }
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        ArrayList<Integer> list1=new ArrayList();
        ArrayList<Integer> list2=new ArrayList();
    findLeaf(root1,list1);
        findLeaf(root2,list2);
        return list1.equals(list2);
    }
}