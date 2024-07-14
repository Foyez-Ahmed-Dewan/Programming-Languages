#include<iostream>
#include<math.h>
using namespace std;

class Circuit{
    private:
        double real;
        double img;
    public:
    Circuit(){
        real = 0;
        img = 0;
    }
    Circuit(int a,int b){
        real = a;
        img = b;
    }
    //methods
    double getreal(){return real;}
    double getimg(){return img;}
    void display(){
        cout<< real << "+ j("<<img <<")"<<endl;
    }
    //overloading operator
    Circuit operator+(const Circuit &rhs){
        Circuit temp;
        temp.real = real+rhs.real;
        temp.img = img +rhs.img;
    return temp;
    }
    Circuit operator/(const Circuit &rhs){
        double reall = (real*(rhs.real) + img*(rhs.img)) * pow((pow(rhs.real,2)+pow(rhs.img,2)),-1);
        double imgg = (img * rhs.real - real * rhs.img) * pow((pow(rhs.real,2)+ pow(rhs.img,2)),-1);
        Circuit temp (reall,imgg);
    return temp;
    }
};

int main(){
    Circuit z1 (3,4);
    Circuit z2 (4,-3);
    Circuit z3 (0,6);

    Circuit V (100,50);
    Circuit Z;

    Z = z1 + z2 + z3;

    Circuit I;
    I = V / Z;
    
    I.display();

    return 0;
}