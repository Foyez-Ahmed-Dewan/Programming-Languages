#include <iostream>
using namespace std;

class A {
public:
	int a;
	A() 
	{
		a = 10;
	}
};

class B : virtual public  A {

};

class C : virtual public A {
};

class D : public B, public C {
};

int main()
{
	D obj;
	cout << "a = " << obj.a << endl;

	return 0;
}
