#ifndef STUDENT_H
#define STUDENT_H

class Student
{
private: 
//attributes
    std::string name;
    int id;
    double cgpa;
public:
//method
    void get_info();
    void set_name(std::string nam){
        name=nam;
    }
    std::string get_name();
    int get_id();
    double get_cg();
//constructor
// Student();
// Student(std::string nam);
// Student(std::string nam,int ide);
// Student(std::string name,int ide,double cg);
Student(std::string name_val ="NONE", int id_val=0,double cg=0);
//copy constructor
Student(const Student &source);
//destructor
~Student();

};

#endif