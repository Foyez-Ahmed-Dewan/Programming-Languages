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


        Int &operator++(){
            x++;
        return *this;
        }
        
        Int operator++(int);
        Int operator+(const Int &rhs){
            Int temp;
            temp.x = x + rhs.x;

        return temp;
        }
        
        bool operator==(const Int &rhs){
            if(this->x != rhs.x)
                return false;
        return true;
        }

        Int &operator+=(const Int &rhs){
            x = x + rhs.x;
        return *this;
        }

        friend istream &operator>>(istream &input,Int &rhs);
        friend ostream &operator<<(ostream &output, const Int &rhs);
};

istream &operator>>(istream &input,Int &rhs){
    input>> rhs.x;
return input;
}
ostream &operator<<(ostream &output,const Int &rhs){
    output<< "X = " << rhs.x;
return output;
}
Int Int::operator++(int){
    Int temp;
    temp.x = x;
    x++;
return temp;
}
int main(){
    Int a ,b;
    cin>> a >> b;
    Int c = a + b;
    cout<< c <<endl;
    
    (a == b) ? cout<< "Equal" <<endl : cout<< "Not equal" <<endl;

    Int d = ++c;
    cout<< c <<endl;
    cout<< d <<endl;

    Int e = c++;
    cout<< c <<endl;
    cout<< e <<endl;

    Int x (30);
    Int y (40);
    x += y;
    cout<< x <<endl;

    return 0;
}