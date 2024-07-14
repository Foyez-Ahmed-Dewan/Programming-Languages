#include<bits/stdc++.h>
using namespace std;

class base
{
public:
    void virtual area(double rad=0);
};

class ractangle:public base
{
    void area(double rad=0)
    {
        double width,length;
        cin>>width>>length;
        cout<<width*length<<endl;
    }
};

class circle:public base
{
    void area(double rad=0)
    {
        cout<<3.14*rad*rad<<endl;
    }
};
int main()
{
    base *p;
    circle obj1;
    ractangle obj2;
    p=&obj1;
    p->area(4);
    p=&obj2;
    p->area();
}