#include<iostream>
using namespace std;

class coord{
    private:
        int x;
    public:
        coord(int a){x=a;}
        friend int operator--(coord &obj);
        friend int operator--(coord &obj,int);
};

int operator--(coord &obj){
    int c = obj.x;
    c=c-1;
    obj.x = c;
return c;
}

int operator--(coord &obj,int){
    int c =obj.x;
    obj.x = obj.x -1;
return c;
}

int main(){
    coord c (10);
    c--;
    coord d = c--;
    coord e = --c;
    
    return 0;
}