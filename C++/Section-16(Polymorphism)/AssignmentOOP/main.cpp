#include<bits/stdc++.h>
using namespace std;

class Employee{
    public:
        string name;
        int id;
        int age;
        double salary;
        //constructor
        Employee()
            : name {"None"}, id {0},age {0}, salary {0}{}
        Employee(string nam,int i,int ag,double sal)
            : name {nam}, id {i},age {ag}, salary {sal}{}
        //methods
        void display(){
            cout<< "\t****Employee Details****" <<endl;
            cout <<"Name  : "<< name <<endl;
            cout<< "Id    : "<< id <<endl;
            cout<< "Age   : "<< age <<endl;
            cout<< "Salary: "<< salary <<endl;
        }

};

class Manager: public Employee{
    private:
        int cnt = 0;
    public:
    //employee list under a manager
     Employee employeeList [10];
    //constructor
    Manager(string nam,int i,int ag,double sal)
        :Employee(nam,i,ag,sal){}

    //adding new Employee
    void addEmployee(const Employee &obj){
        if(cnt >=9){
            cout<< "Limit exceed" <<endl;
        }
        employeeList [cnt] = obj;
        cnt++;
    }
    //deleting an existing employee 
    void deleteEmployee(const Employee &obj){
        Employee e;
        bool flag = false;
        int i = 0;
        for(i = 0; i<cnt; i++){
            e = employeeList [i];

            if(e.name == obj.name && e.age == obj.age && e.id == obj.id && e.salary == obj.salary){
                Employee temp ;
                employeeList[i] = temp;
                cout<< "Deleted Successfully" <<endl;
                flag = true;
                break;
            }else{
                cout<< "This employee doesnot exist under this manager" <<endl;
            }
        }

        if(flag){
            for(; i<cnt-1; i++){
                employeeList[ i ] = employeeList [i+1];
            }
            cnt--;
        }
    }
    //this function shift "em" employee to "man1" manager from "this" manager
    void FromShiftTo(const Employee &em,Manager &man1){
        this->deleteEmployee(em);   //first delete name from current manager list
        man1.addEmployee(em);   //then give appointment under new manager
    }   
    //displaying all information of Manager and List
    void display(){
        cout<< endl;
        cout<< "\t****Manager Details*****" <<endl;
            cout <<"Name  : "<< name <<endl;
            cout<< "Id    : "<< id <<endl;
            cout<< "Age   : "<<age <<endl;
            cout<< "Salary: "<< salary <<endl;
        if(cnt == 0){
            cout<< "No employee works under this manager" <<endl;
        }else{
            cout<< "\t****Employee Details****";
            Employee e;
            for(int i = 0; i<cnt; i++){
                e = employeeList [i];
                cout<< endl;
                cout<< "Employee : "<< i+1 <<endl;
                cout <<"Name  : "<< e.name <<endl;
                cout<< "Id    : "<< e.id <<endl;
                cout<< "Age   : "<< e.age <<endl;
                cout<< "Salary: "<< e.salary <<endl;
            }
        }
    }
};


int main(){
    Employee emp1 ("Emp-1",1,20,200);
    // emp1.display();
    Employee emp2 ("Emp-2",11,10,200);
    // emp2.display();
    Employee emp3 ("Emp-3",20,11,1000);
    
    Manager man1 ("Foyez",10,20,200);
    Manager man2 ("Dewan",10,20,10000);

    man1.addEmployee(emp1); //adding employee emp1 under man1 manager
    man1.addEmployee(emp2); //adding employee emp2 under man1 manager
    man1.display();

    man1.deleteEmployee(emp1);  //deleting employee emp1 from under manager man1
    man1.display();
 
    man1.addEmployee(emp3);     //addding new employeee under man1 manager
    man1.display();

    man2.display();
    man1.FromShiftTo(emp2,man2);   //shifting an employee emp2 to manager man2 from manager man1
    man1.display();
    man2.display();

    return 0;
}