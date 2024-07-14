#include<iostream>
using namespace std;

int main()
{
    int miles,gallons;
    cout<<"Enter how many miles driven: ";      cin>> miles;
    cout<<"Enter how many gallons needed: ";    cin>> gallons;

    // double miles_per_gal= miles/gallons;
    try
    {
        if(gallons==0)
            throw 0;
    double miles_per_gal= (double)miles/gallons;
    cout<<"Result: "<<miles_per_gal<<endl;
    }
    
    catch(int &ex)
    {
        cout<<"Dividing by Zero is not possible"<<endl;
    }
    cout<<"Bye"<<endl;

    return 0;
}