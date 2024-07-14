#include<bits/stdc++.h>
using namespace std;


int main(){
    int n=0,sum=0,a=0,b=0,temp=0;
    vector<int >vec;
    cin>>n;
    for(int i=0;i<n;i++)
        cin>>vec[i];

    for(int i=0;i<n-1;i++){
        for(int j=i+1;j<n;j++){
            sum=vec[i]+vec[j];
            if(sum%2==1){
                sum=0;
                temp=vec[i];
                vec[i]=vec[j];
                vec[j]=temp;
    
            }
        }
    }
    for(int i=0;i<n;i++){
        cout<<vec[i]<<endl;
    }
    return 0;
}