#include<bits/stdc++.h>
using namespace std;

int main(){
    int n=0,k=0,count=0,div=0,num=0;
    cin>>n>>k;
    vector<int>vec;
    for(int i=1;i<=n/2;i++){
        if(n%i==0){
            count++;
            vec.push_back(n/i);
        }
        
    }
    count++;
    std::sort(vec.begin(),vec.end());
    if(count<k)
        cout<<-1<<endl;
    else{
        cout<<vec[k-2]<<endl;
    }

    return 0;
}