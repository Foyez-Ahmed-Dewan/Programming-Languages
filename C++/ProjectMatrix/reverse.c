#include<stdio.h>
int main(){

int n;
scanf("%d",&n);
int arr[n],arr_ou[n];
for(int i=0;i<n;i++){
    scanf("%d",&arr[i]);
}
for(int i=0;i<n;i++){
    arr_ou[i]=arr[n-i-1];
    
}

for(int i=0;i<n;i++){
    printf("%d ",arr_ou[i]);
}
    return 0;
}