#include<iostream>
#include<string>
using namespace std;

double calculate_mpg(int miles,int gallons)
{
    if(gallons==0)
        throw 0;
    if(miles<0 or gallons<0)
        throw string("Negative value error");   //***
    return (double)miles/gallons;
}

int main()
{
    int miles,gallons;
    cout<<"Enter how many miles driven: ";      cin>> miles;
    cout<<"Enter how many gallons needed: ";    cin>> gallons;
    try

    {
        double miles_per_gal= calculate_mpg(miles,gallons);
        cout<<"Result: "<<miles_per_gal<<endl;      
    }

    
    catch(int &ex)
    {
        cout<<"Dividing by zero is not possible"<<endl;
    }

    catch(string ex){
        cout<< ex <<endl;
    }
    
    catch(...){
        cout<<"Exception Occurs"<<endl;
    }
    cout<<"Bye"<<endl;
    // catch(...){
    //     cout<<"Exception Occurs"<<endl;
    // }

    return 0;
}