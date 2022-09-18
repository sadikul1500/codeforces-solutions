//got idea from epsilon_573
#include<iostream>
#include<map>
#include<vector>
#include<algorithm>

typedef long long ll;
#define endl "\n"

using namespace std;

bool sortByVal(const pair<ll,ll> &a, const pair<ll,ll> &b){
    return a.second >b.second;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    int t;
    cin>>t;
    
    while(t--){
        int n;
        cin >> n;

        vector<ll> a(n+1, 0);//, prefixSum(n+1, 0);
        map<ll,ll> prefixSum;

        for(int i=1; i<=n; i++){
            cin>>a[i];
            prefixSum[i] = prefixSum[i-1] + (a[i]<i);                       
        }
        ll count = 0;
        
        for(int i=n; i>1; i--){
            count += (a[i]<i) * prefixSum[a[i]-1];
        }

        cout<<count<<"\n";

    }
}
// int main(){
//     ios_base::sync_with_stdio(false);
//     cin.tie(0);

//     int t;
//     cin>>t;
//     while(t--){
//         int n;
//         cin>>n;

//         // vector<ll> a(n+1);
//         map<ll, ll> m;
//         ll number;
//         // cout<<m[1]<<endl;
//         for(int i=1; i<=n; i++){
//             cin>>number;
//             m[i] = number;
//         }

//         vector<pair<ll,ll>> a;
//         for(auto item: m){
//             a.push_back(make_pair(item.first,item.second));
//         }
//         sort(a.begin(), a.end(), sortByVal);

//         map<ll, ll> cum;
//         // int pointer = 0;
//         for(auto item : a){
//             if(item.second < item.first){//second: value, first:key
//                 cum[item.second] += 1 + cum[item.first];
//                 // pointer = item.second;
//             }
//             // cout<<item.first<<" "<<item.second<<"\n";
//         }

//         ll count = 0;
//         for(auto item: m){ //index:value
//             if(item.second < item.first){
//                 count += cum[item.first+1];
//             }
//         }

//         // for(int i=1; i<=n; i++){
//         //     if(a[i] >= i) continue;
//         //     for(int j=i+1; j<=n; j++){
//         //         if(i < a[j] && a[j] < j){
//         //             count++;
//         //         }
//         //     }
//         // }

//         cout<<count<<"\n";
//     }
// }