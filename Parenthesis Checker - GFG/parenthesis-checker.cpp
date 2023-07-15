//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution
{
    public:
    //Function to check if brackets are balanced or not.
    bool ispar(string x)
    {
        // Your code here
        stack<char> st;
        int count = 0;
        for(int i = 0 ; i< x.length(); i++){
            if(x[i] == '{' || x[i] == '(' || x[i] == '['){
                st.push(x[i]);
                count++;
            }
            else if(!st.empty()){
                if(st.top() == '(' && x[i] == ')') {st.pop();count++;}
                else if(st.top() == '{' && x[i] == '}') {st.pop();count++;}
                else if(st.top() == '[' && x[i] == ']') {st.pop();count++;}
                
            }
            else return false;
        }
        return (st.empty() && count == x.length());
    }

};

//{ Driver Code Starts.

int main()
{
   int t;
   string a;
   cin>>t;
   while(t--)
   {
       cin>>a;
       Solution obj;
       if(obj.ispar(a))
        cout<<"balanced"<<endl;
       else
        cout<<"not balanced"<<endl;
   }
}
// } Driver Code Ends