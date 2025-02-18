#include<iostream>
using namespace std;

class Base1
{
    public:
        Base1(){
            cout<< "Constructor for base-1 class"<<endl;
        }
        ~Base1(){
            cout<<" Destructor for base-1 class"<<endl;
        }
        void display(){cout<<"Display->Base 1"<<endl;}
};

class Base2
{
    public:
        Base2(){
            cout<<"Constructor for base-2 class"<<endl;
        }
        ~Base2(){
            cout<<"Destructor for base-2 class"<<endl;
        }
        void display(){cout<<"Display->Base 2"<<endl;}
};

class Derived: public Base1, public Base2
{
    public:
        Derived(){
            cout<<"Constructor for derived Class"<<endl;
        }
        ~Derived(){
            cout<<"Destructor for derived class"<<endl;
        }
        // void display(){cout<<"Display->Derived"<<endl;}
};

int main()
{
    Derived obj;
    // obj.display();

    //Ambiguity in multiple inheritance and solution
    // obj.display(); //Error because compiler does not know which display function to call?
    // obj.Base1::display(); //solution: **object.(which class function you want to call)::(function name);**

    return 0;
}