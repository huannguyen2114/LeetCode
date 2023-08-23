/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> preorderTraversalHelper(TreeNode* root, vector<int>& temp) {
        if(root == NULL){
            return temp;
        }
        temp.push_back(root->val);
        preorderTraversalHelper(root->left, temp);
        preorderTraversalHelper(root->right,temp);
        return temp;
    }
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> temp;
        return preorderTraversalHelper(root, temp);
    }
};