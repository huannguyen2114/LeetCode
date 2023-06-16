class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l=0;
        int r=0;
        int sum=0;
        while(r< prices.size()){
           if(prices[r] > prices[l]){
               sum = max(sum, prices[r] - prices[l]);
           }
            else l=r;
            ++r;
        }
        return sum;
    }
};