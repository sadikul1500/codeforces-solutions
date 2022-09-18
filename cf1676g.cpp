// C++ program to print DFS traversal from
// a given vertex in a given graph
#include <iostream>
#include<map>
#include<list>
#include<string>

using namespace std;

void DFS(int v, map<int, list<int>> &adj, map<int, bool> &visited, map<int, int> &count, string s)
{
    
    visited[v] = true;
    if(s[v-1] == 'B'){
        count[v]--;
    }
    else count[v]++;
    
    for(auto node: adj[v]){
        if(!visited[node]){
            DFS(node, adj, visited, count, s);
            count[v] += count[node];
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin>>t;

    while(t--){
        int n, vertex, ans =0;
        string s;
        cin>>n;
        
        map<int, bool> visited;
        map<int, list<int>> adj;
        map<int, int> count;

        for(int i=0; i<=n-2; i++){
            cin>>vertex;
            adj[vertex].push_back(i+2);
        }
        
        getline(cin, s);
        getline(cin, s);
        // cout<<"called\n";
        DFS(1, adj, visited, count, s);
        // cout<<"call finished\n";
        for(auto x :count){
            if(x.second == 0) ans++;
        }
        cout<<ans<<"\n";


    }
}