#include<iostream>
using namespace std;

class base {
    public:
    int i;
    base(){}
    base(int x){i=x;}
    int geti(){return i;}
    virtual void func(){
        cout<<"Using base version of func(): "<< i <<endl;
    }
};
class derived1: public base{
    public:
    derived1(){}
    derived1(int x)
        : base(x+90){}
    void func(){
        cout<< "Using derived1's version of func(): "<< geti() <<endl;
    }
};

class derived2: public base{
    public:
    derived2(){}
    derived2(int x)
        : base(x+10){}
    void func(){
        cout<< "Using derived2's version of func(): "<< geti() <<endl;
    }
};


int main(){
    base *p;
    base ob (10);
    derived1 d_ob1 (10);
    derived2 d_ob2 (10);

    p = &ob;
    p->func();
    p = &d_ob1;
    p->func();
    p = &d_ob2;
    p->func();
    
    return 0;
}