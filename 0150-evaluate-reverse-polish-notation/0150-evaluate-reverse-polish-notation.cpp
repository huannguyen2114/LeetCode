bool isNum(string s){
    if(s == "+" || s=="-" || s=="*" || s=="/") return false;
    return true;
}

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int>stk;
        for(int i =0; i< tokens.size(); i++){
            if(isNum(tokens[i])){
                stk.push(stoi(tokens[i]));
            }
            else{
                int a = stk.top();
                stk.pop();
                int b = stk.top();
                stk.pop();
                if(tokens[i] == "+") stk.push(a+b);
                if(tokens[i] == "-") stk.push(b-a);
                if(tokens[i] == "*") stk.push(a*b);
                if(tokens[i] == "/") stk.push(b/a);
            }
        }
        int res = stk.top();
        stk.pop();
        return res;
        
    }
};