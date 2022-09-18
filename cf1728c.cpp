// #include<iostream>
// #include<vector>
// #include<cmath>
// #include<algorithm>
// #include<map>

// #define ll long long int

// using namespace std;

// int myLog(long long int x){
//     int result = log10(x);
    
//     return result + 1;
// }

// int main(){
//     int t;
//     cin>>t;

//     while(t--){
//         int n, operations = 0;
//         long long int num;
//         cin>>n;
//         vector<long long int > a;
//         vector<long long int > b;
//         map<ll, ll> freqa, freqb;

//         for(int i=0; i<n; i++){
            
//             cin>>num;
//             a.push_back(num);
//             freqa[num]++;
//         }
        

//         for(int i=0; i<n; i++){
            
//             cin>>num;
//             b.push_back(num);
//             freqb[num]++;
//         }
//         //remove similar items
//         for(auto x :freqa){
//             int first = x.second;
//             int second = freqb[x.first];
//             int mini = min(first, second);

//             freqa[x.first] -= mini;
//             freqb[x.first] -= mini;
//         }
//         //digital log
//         for(auto x :freqa){
//             if(x.first > 9){
//                 ll new_num = log10(x.first) +1; 
//                 freqa[new_num] += x.second;
//                 operations += x.second;
//                 freqa[x.first] = 0;
//                 // cout<<x.second<<endl;
//             }
//         }
//         // cout<<"okk1"<<endl;
//         //digital log
//         for(auto x :freqb){
//             if(x.first > 9){
//                 ll new_num = log10(x.first) +1; 
//                 freqb[new_num] += x.second;
//                 operations += x.second;
//                 freqb[x.first] = 0;
//                 // cout<<x.second<<endl;
//                 // operations += 1;
//             }
//         }
//         // cout<<operations<<endl;
//         //remove similar items
//         for(auto x :freqa){
//             int first = x.second;
//             int second = freqb[x.first];
//             int mini = min(first, second);

//             freqa[x.first] -= mini;
//             freqb[x.first] -= mini;
//         }

//         for(auto x:freqa){
//             if(x.first > 1 && x.second > 0)
//             operations += x.second;
//         }

//         for(auto x:freqb){
//             if(x.first > 1 && x.second > 0)
//             operations += x.second;
//         }
        
//         // for(long long int  value: a){
            
//         //     vector<long long int>::iterator it = find(b.begin(), b.end(), value);
//         //     // cout<<it<<endl;
            
//         //     if(it != b.end()){
                
//         //         a.erase(find(a.begin(),a.end(),value));
//         //         b.erase(it);
//         //     }
//         // }
        
        
//         // int operations = 0;
        
//         // for(int i = 0; i<a.size(); i++){
//         //     if(a[i] > 9){
//         //         a[i] = myLog(a[i]);
//         //         operations += 1;
//         //     }
//         //     if(b[i] > 9){
//         //         b[i] = myLog(b[i]);
//         //         operations += 1;
//         //     }

//         // }
//         // for (auto val: a){
//         //     cout<<val<< " ";
//         // }
//         // cout<<endl;

//         // for (auto val: b){
//         //     cout<<val<< " ";
//         // }
//         // cout<<endl;

//         // for(long long int  value: a){
            
//         //     vector<long long int>::iterator it = find(b.begin(), b.end(), value);
            
//         //     if(it != b.end()){
//         //         a.erase(find(a.begin(),a.end(),value));
//         //         b.erase(it);
                
//         //     }
//         //     else if (value > 1){
//         //         operations += 1;
//         //     }
//         // }
//         // for (auto val: a){
//         //     cout<<val<< " ";
//         // }
//         // cout<<endl;

//         // for (auto val: b){
//         //     cout<<val<< " ";
//         // }
//         // cout<<endl;
//         // for(int i = 0; i<b.size(); i++){
//         //     if(b[i] > 1)
//         //         operations += 1;
//         // }
        
//         cout<<operations<<endl;

        
//     }

// }



// Online C++ compiler to run C++ program online
// #include <iostream>
// #include <algorithm>
// using namespace std;
// int main() {
//     int n;
//     cin>>n;
//     int x[n];
//     int y[n];
//     int m[n];
    
//     for (int i=0; i<n; i++) cin>>x[i];
//     for (int i=0; i<n; i++) cin>>y[i];
//     // cout<<"oo----";
//     for (int i=0; i<n; i++) m[i] = y[i]-x[i];
    
//     sort(m,m+n);
//     int xero = 0,grp=0,posi=0;
//     int negpos,pospos;
//     for (int i=n-1; i>-1; i--)
//         if(m[i]<0){
//             negpos = i;
//             break;
//         }
//         pospos=negpos+1;
//         // int negtive,postive;
//         while(negpos>-1){
//             int neg = m[negpos],pos=0;
//             for(int i=pospos;i<n;i++){
//                 if(m[i]==0) {
//                     xero+=1;
//                     continue;
//                 }
//                 else{
//                     pos+=m[i];
//                     // cout<<neg<<" "<<pos<<endl;
//                     if(pos>=neg*-1) {
//                         grp+=1;
//                         negpos--;
//                         pospos=i+1;
//                         break;
//                     }
//                 }
//             }
            
//         }
//         for(int i=pospos;i<n;i++)
//         if(m[i]>0) xero++;
//         cout<<xero/2+grp;
//         // cout<<xero/2<<" "<<grp;
// }