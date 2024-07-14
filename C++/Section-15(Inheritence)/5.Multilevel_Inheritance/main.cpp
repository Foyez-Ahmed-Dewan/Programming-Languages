#include<iostream>
using namespace std;

class Base
{
    public:
    Base(){
        cout<<"Constructor for Base class is called"<<endl;
    }
    void display(){cout<<"Display->Base"<<endl;}
};

class Derived1: public Base
{
    public:
    Derived1(){
        cout<< "Constructor for Derived-1 class is called" <<endl;
    }
    void display(){cout<<"Display->Derived 1"<<endl;}
};

class Derived2: public Derived1
{
    public:
        Derived2(){
            cout<< "Constructor for Derived-2 class is called" <<endl;
        }
        // void display(){cout<<"Display->Derived 2"<<endl;}
};
int main()
{
    // Base a;
    // a.display();

    // Derived1 b;
    // b.display();

    Derived2 c;
    c.display();

    return 0;
}