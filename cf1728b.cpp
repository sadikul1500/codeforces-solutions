#include<iostream>

using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        if(n%2){
            for(int i=n-2; i>=4; i--){
                cout<<i<<" ";
            }
            cout<<"1 2 3 "<<n-1<<" "<<n<<endl;
        }
        else{
            // int temp = n/2;
            for(int i=n-2; i>=1; i--){
                cout<<i<<" ";
            }
            // cout<<1<<" ";
            // for(int i=temp+1; i<=n; i++){
            //     cout<<i<<" ";
            // }
            cout<<n-1<<" "<<n<<endl;
        }
    }
}