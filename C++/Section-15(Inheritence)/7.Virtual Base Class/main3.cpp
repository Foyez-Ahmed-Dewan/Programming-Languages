#include<bits/stdc++.h>
using namespace std;

class A
{
    private:
        int a;
    public:
        int getA(){return a;}
        A(){}
        A(int x){a=x;}
};

class B : public A
{
    private:
        int b;
    public:
        int getB(){return b;}
        B(){}
        B(int x,int y)
            :A (x) , b {y}{}
};

class C : public B
{
    private:
        int c;
    public:
        C(){}
        C(int x,int y, int z)
            :B(x,y), c {z}{}
        int getC(){return c;}
        int sum(){
            int a=getA();
            int b=getB();
            int cx=c;
        return a+b+cx;
        }
};



int main()
{
    C c (10,20,30);
    cout<< c.sum() <<endl;


    return 0;
}