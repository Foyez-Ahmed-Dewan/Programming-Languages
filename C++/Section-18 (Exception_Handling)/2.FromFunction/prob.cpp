#include<iostream>
using namespace std;

double calculate_mpg(int miles,int gallons)
{
    if(gallons==0)
        throw 0;
    return (double)miles/gallons;
}

int main()
{
    int miles,gallons;
    cout<<"Enter how many miles driven: ";      cin>> miles;
    cout<<"Enter how many gallons needed: ";    cin>> gallons;

    // double miles_per_gal= miles/gallons;
    
    double miles_per_gal= calculate_mpg(miles,gallons);
    cout<<"Result: "<<miles_per_gal<<endl;
        
    
    cout<<"Bye"<<endl;

    return 0;
}