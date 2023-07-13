class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        stack<pair<int, int>> stk;
        vector<int> res(n);
        for(int i=0; i< n ; i++){
            int currTemp = temperatures[i];
            int currDay = i;
            while(!stk.empty() && stk.top().second < currTemp){
                int preTemp = stk.top().second;
                int preDay = stk.top().first;
                stk.pop();
                res[preDay]  = currDay - preDay;
            }
            stk.push({currDay, currTemp});
        }
        return res;}
};