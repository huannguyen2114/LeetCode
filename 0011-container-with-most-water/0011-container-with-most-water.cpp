class Solution {
public:
    int maxArea(vector<int>& height) {
        int pointerA = 0;
        int pointerB = height.size()-1;
        int max = -1;
        while (pointerA < pointerB){
            int temp = min(height[pointerA], height[pointerB]) * (pointerB-pointerA);
            if(temp > max){
                max = temp;
            }
            else{
                if(height[pointerA] > height[pointerB]){
                    pointerB--;
                }
                else{
                    pointerA++;
                }
            }
        }
        return max;
    }
    
};