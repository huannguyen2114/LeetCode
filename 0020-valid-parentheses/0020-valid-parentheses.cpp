class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        int count = 0;
        for(int i = 0 ; i< s.length(); i++){
            if(s[i] == '{' || s[i] == '(' || s[i] == '['){
                st.push(s[i]);
                count++;
            }
            else if(!st.empty()){
                if(st.top() == '(' && s[i] == ')') {st.pop();count++;}
                else if(st.top() == '{' && s[i] == '}') {st.pop();count++;}
                else if(st.top() == '[' && s[i] == ']') {st.pop();count++;}
                
            }
            else return false;
        }
        cout<<count<<" ";
        return (st.empty() && count == s.length());
    }
};