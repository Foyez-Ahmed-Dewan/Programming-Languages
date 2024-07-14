#include<bits/stdc++.h>
using namespace std;

class Int{
    private:
        int x ;
    public:
        Int()
            : x {0}{}
        Int(int a)
            : x {a}{}

        void display(){
            cout<< "X = "<< x  <<endl;
        }

        friend Int &operator++(Int &lhs);
        friend Int operator++(Int &lhs,int);

        friend Int &operator+=(Int &lhs,const Int &rhs);
        friend Int operator+(const Int &lhs,const Int &rhs);

        friend istream &operator>>(istream &input,Int &rhs);
        friend ostream &operator<<(ostream &output,const Int &rhs);
        
       
};

istream &operator>>(istream &input,Int &rhs){
    input >> rhs.x;
return input;
}

ostream &operator<<(ostream &output,const Int &rhs){
    output << "X = " << rhs.x;
return output;
}
Int &operator++(Int &lhs){
    lhs.x ++;
    
return lhs; 
}
Int operator++(Int &lhs,int){
    Int temp ;
    temp.x = lhs.x;
    lhs.x ++;
return temp;
}

Int &operator+=(Int &lhs,const Int &rhs){
    lhs.x = lhs.x + rhs.x;
return lhs;
}

Int operator+(const Int &lhs, const Int &rhs){
    Int temp ;
    temp.x = lhs.x + rhs.x;
return temp;
}


int main(){
    Int a (20),b (30);
    Int c = a + b;
    c.display();
    
    Int d = ++ a;
    d.display();
    a.display();

    Int e = a++;
    a.display();
    e.display();

    a+=e;
    a.display();
    e.display();

    Int f,g;
    cin>> f >> g;
    cout<< f << g <<endl;

    return 0;
}