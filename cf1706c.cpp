#include<iostream>
#include<vector>
#include<cmath>
#include<map>

#define ll long long

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin>>t;

    while(t--){
        int n;
        cin>>n;
        vector<ll> h(n),dp(n);

        for(int i=0; i<n; i++){
            cin>>h[i];
            dp[i] = 0;
        }

        for(int i=1; i<n-1; i++){
            if(h[i] > h[i+1] && h[i] > h[i-1]){
                dp[i] = 0;
                // count++;
            }
            else{
                dp[i] = max(h[i-1], h[i+1]) - h[i] + 1; 
            }
        }

        if(n%2){
            ll summ = 0;
            for(int i=1; i<n; i++){
                summ += dp[i];
                i++;
            }
            cout<<summ<<"\n";
        }
        else{
            ll sum_odd = 1e18, sum_even = 1e18;
            map<int, ll> summ;
            for(int i=n-1; i>=1; i--){
                if(i%2){
                    if(sum_odd >= 1e18){
                        sum_odd = 0;
                    }
                    sum_odd += dp[i];
                    summ[i] = sum_odd;
                }
                //  sum_odd += dp[i];
                else{
                    if(sum_even >= 1e18) sum_even = 0;
                    sum_even += dp[i];
                    summ[i] = sum_even;
                }
            }
            ll mini = min(sum_odd, sum_even);
            ll sum2 = 0;
            for(int i=1; i<=n-1; i++){
                sum2 += dp[i];
                if(i+3 <=n-1 && sum2 + summ[i+3] < mini){
                    mini  = sum2 + summ[i+3];
                }
                i++;
            }
            cout<<mini<<"\n";

        }
        // dp[0] = 0;
        // dp[1] = 0;
        // int count = 0;
        // for(int i=1; i<n-1; i++){
        //     if(h[i] > h[i+1] && h[i] > h[i-1]){
        //         dp[i] = 0;
        //         count++;
        //     }
        //     else{
        //         dp[i] = max(h[i-1], h[i+1]) - h[i] + 1; 
        //     }
        // }
        // if(count >= ceil((n-2)/2) && count > 0){
        //     cout<<count<<endl;
        //     cout<<"0\n";
        // }
        // else{
        // ll sum_odd = 1e18, sum_even = 1e18;
        // for(int i=1; i<n-1; i++){
        //     if(i%2){
        //         if(sum_odd >= 1e18){
        //             sum_odd = 0;
        //         }
        //         sum_odd += dp[i];
        //     }
        //     //  sum_odd += dp[i];
        //     else{
        //         if(sum_even >= 1e18) sum_even = 0;
        //         sum_even += dp[i];
            
        //     }
        // }
        // cout<<min(sum_odd, sum_even)<<"\n";
        // cout<<sum_odd<<" "<<sum_even<<" "<<count<<"\n";
        // }
        
    }
}