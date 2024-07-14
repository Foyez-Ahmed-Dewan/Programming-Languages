#include<bits/stdc++.h>
using namespace std;

class A
{
    public:
        A(){cout<<"class A"<<endl;}
         void show(){
            cout<<"Show-A"<<endl;
        }
};
class B:virtual public A{
    public:
    B(){cout<<"class B"<<endl;}
    // void show(){
    //     cout<<"Show-B"<<endl;
    // }
};

class C:virtual public A{
    public:
    C(){cout<<"class C"<<endl;}
     void show(){
            cout<<"Show-C"<<endl;
        }
};

class D: public B,public C{
    public:
    D(){
        cout<< "class D"<<endl;
    }
    // void show(){
    //     cout<<"Show-D"<<endl;
    // }
};



int main()
{
    D d;
    d.show();

    return 0;
}