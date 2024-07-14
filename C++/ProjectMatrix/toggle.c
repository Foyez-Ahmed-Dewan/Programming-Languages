#include<stdio.h>
int main(){
    char s[100];
    fgets(s,100,stdin);
    int i=0,count=0;
    while(s[i] != '\0'){
        if(s[i]>='A' && s[i]<='Z')
            s[i]=s[i]+32;
        else if(s[i]>='a' && s[i]<='z')
            s[i]=s[i]-32;
        i++;
        count++;
    }
    for(int i=0;i<count;i++){
        printf("%c",s[i]);
    }

    return 0;
}