class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> sumMap;
        vector<int> res;
        for(int i=0; i<nums.size();i++){
            int complement= target - nums[i];
            if(sumMap.find(complement) != sumMap.end()){
                res.push_back(sumMap[complement]);
                res.push_back(i);
                break;
            }
            sumMap.insert({nums[i], i});
        }
        return res;
    }
};