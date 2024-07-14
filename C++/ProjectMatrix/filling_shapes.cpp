#include<iostream>
using namespace std;

int main(){
    int n=0,j=0,total_way=1;
    cin>>n;
    j=n/2;
    if(n%2 == 1)
        cout<<0<<endl;
    else {
        for(int i=0;i<j;i++)
            total_way*=2;

            cout<<total_way<<endl;
    }
    

    return 0;
}