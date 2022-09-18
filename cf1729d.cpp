// Online C++ compiler to run C++ program online
#include <iostream>
#include<vector>
#include<map>
#include<cmath>
#include<string>
#include<algorithm> 

#define ll long long int 

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    // Write C++ code here
    // std::cout << "Hello world!";
    int t;
    cin>>t;
    
    while(t--){
    
        int n;
        cin>>n;
        vector<ll> x(n), y(n), pos, neg;
        map<ll, ll> freq;
        
        for(int i=0; i<n; i++){
            cin>>x[i];
        }
        for(int i=0; i<n; i++){
            cin>>y[i];
            if(y[i]-x[i] > 0){
                pos.push_back(y[i]-x[i]);
            }
            else if(y[i]-x[i] < 0){
                neg.push_back(y[i]-x[i]);
            }
            else{
                freq[0] ++;
            }
            // cout<<z[i]<<endl;
        }
        
        sort(pos.begin(), pos.end());
        sort(neg.begin(), neg.end()); //,greater<ll>()
        ll sum = 0;
        ll ans = 0;
        ll k = 0;

        int iter = pos.size() -1;
        while(neg.size()> 0 && iter >=0){
            if(pos[iter] >= -1 * neg[0]){
                ans += 1;
                neg.erase(neg.begin());
                iter -= 1;
            }
            else{
                neg.erase(neg.begin());
            }
        }
        k = pos.size() - ans + freq[0];
        // for(int i=pos.size()-1; i>=0; i--){
        //     if(pos[i] >= -1 * )

        // }
        // for(int i=0; i<pos.size(); i++){
        //     sum += pos[i];
        //     if(neg.size() == 0){
        //         // k = i+1;
        //       break;  
        //     } 
        //     if(sum >= -1*neg[0]){
        //         ans += 1;
        //         neg.erase(neg.begin());
        //         sum = 0;
        //         k = i+1;
        //     }
        //     cout<<"negative "<<neg[0]<<endl;
            
        // }
        // cout<<pos.size()<<" "<<freq[0]<<" "<<k<<endl;
        // k = pos.size() - k + freq[0];
        // cout<<"k "<<k<<endl;
        ans += k / 2;
        cout<<ans<<endl;
        // for(auto x :freq){
        //     cout<<x.first<<" "<<x.second<<endl;
        // }
    }
        
        
        
        
        

    return 0;
}