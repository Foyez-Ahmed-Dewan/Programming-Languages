#include<iostream>
using namespace std;

class A{
    private:
        int x = 0;
        static int y;
    public:
        A(int a){
            x = a;
            y++;
        }
        static int getY(){return y;}
};
//initialing static data member outside the class
int A::y = 0;

int main(){
    A c1 (10);  // x = 10, y = 1
    A c2 (20);  //x = 20, y = 2
    cout<< A::getY() <<endl;    //2


    return 0;
}