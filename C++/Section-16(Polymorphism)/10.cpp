#include<iostream>
using namespace std;

class A{
    public:
        virtual void Print()=0;
};

class B:public A{
    public:
        void Print(){
        cout<<"Inside Print() of class B"<<endl;
}
};

int main(){
    // A a; //Error since class A contain pure virtual function hence class A is now abstract class 
    B b;
    b.Print();

    A *p;
    p = &b;
    p->Print();
    

    return 0;
}