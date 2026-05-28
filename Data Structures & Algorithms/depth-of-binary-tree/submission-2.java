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
        Stack<Pair<TreeNode,Integer>> stack = new Stack();
        stack.push(new Pair(root,1));
        int max=0;
        while(!stack.isEmpty()) {
            Pair<TreeNode,Integer> pair = stack.pop();
            TreeNode cur = pair.getKey();
            int depth = pair.getValue();
            if(cur.left==null && cur.right==null) {
                max = Math.max(max, depth);
            }
            if(cur.left!=null) {
                stack.push(new Pair(cur.left, depth+1));
            }
            if(cur.right!=null) {
                stack.push(new Pair(cur.right, depth+1));
            }
        }
        return max;
    }
}
