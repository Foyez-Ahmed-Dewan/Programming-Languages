#include<iostream>
#include "Student.cpp"
using namespace std;

int main(){
    Student foyez;
    foyez.set_name("Foyez");
    foyez.get_info();

    Student frank {"Frank",2003062,4};
    frank.get_info();

    Student *asif=new Student("Asif",64);
    asif->get_info();
    delete asif;


    return 0;
}