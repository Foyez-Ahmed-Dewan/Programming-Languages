#include "Student.h"

//methods

void Student::get_info(){
    std::cout<<name<<" "<<id<<" "<<cgpa<<std::endl;
}

//constructor
// Student::Student(){
//     name="None";
//     id=0;
//     cgpa=0;
// }
// //
// Student::Student(std::string nam){
//     name=nam;
//     id=0;
//     cgpa=0;
// }
// //
// Student::Student(std::string nam, int ide)
//     :Student{nam,ide,0}{
//         //constructor body
//     }
Student::Student(std::string nam, int ide, double cg)
    :name {nam}, id {ide}, cgpa{cg}{
        //constructor body
    }
//Copy constructor
Student::Student(const Student &source)
    :Student{source.name,source.id,source.cgpa}{

    }

//destructor
Student::~Student(){
    
}