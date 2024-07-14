#include<bits/stdc++.h>
using namespace std;

int main(){
    int t=0;
    cin>>t;
    while(t>0){
        long long a=0,b=0,c=0,d=0,count=0;
        cin>>a>>b>>c>>d;
        if(a<b)
            count++;
        if(a<c)
            count++;
        if(a<d)
            count++;
        
        cout<<count<<endl;

        t--;
    }
    return 0;
}