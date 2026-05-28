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
    public int maxDepth(TreeNode root) {
        if(root==null) {
            return 0;
        }
        return helper(root);
    }

    public int helper(TreeNode cur) {
        if(cur==null) {
            return 0;
        }
        if(cur.left==null && cur.right==null) {
            return 1;
        }
        return Math.max(helper(cur.left), helper(cur.right))+1;
    }
}
