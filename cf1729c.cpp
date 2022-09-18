#include<iostream>
#include<string>
#include<vector>
#include<cmath>

#define ll long long

using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    ll t;
    cin >>t;
    string s;
    getline(cin, s);

    while(t--){
        // string s;
        getline(cin, s);
        vector<int> steps;
        // cout<<s<<"\n";
        int n = s.length();
        // cout<<n<<"\n";
        int cost = abs(s[0] - s[n-1]);
        cout<<cost<<" ";

        if(s[0] <= s[n-1]){
            
            for(int i=s[0]; i<=s[n-1]; i++){
                char ch = i;
                // cout<<ch<<" ";
                for(int j = 1; j<=n-1; j++){
                    if(s[j] == ch){
                        steps.push_back(j+1);
                        // cout<<j+1<<" ";
                    }
                }
            }
            cout<<steps.size()+1<<"\n"<<"1 ";
            for(auto a: steps){
                cout<<a<<" ";
            }
            cout<<"\n";
            
        }

        else{
            // cout<<"came\n";
            for(int i=s[n-1]; i<=s[0]; i++){
                // char ch = i;
                // cout<<ch<<" ";
                for(int j = n-2; j>=0; j--){
                    if(s[j] == i){
                        steps.push_back(j+1);
                        // cout<<s[j]<<" ";
                    }
                }
                // cout<<"\n";
            }
            cout<<steps.size()+1<<"\n";
            for(int i=steps.size()-1; i>=0; i--){
                cout<<steps[i]<<" ";
            }
            cout<<n<<"\n";
        }

    }

}