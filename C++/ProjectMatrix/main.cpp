#include<bits/stdc++.h>
using namespace std;
void Order_of_matrix(){
    int row=0,col=0;
    
}
void Trace_Matrix(){
    int r=0,c=0,row=0,col=0,trace=0;
    cout<<"Enter row and column of your Matrix respectively: ";
    cin>>r>>c;
    int mat [r][c]={};
    cout<<"Give element row wise:\n";
    for( row=0;row<r;row++){
        for(col=0;col<c;col++){
            cin>>mat[row] [col];

        if(row==col)
            trace+=mat[row][col];
        }
    }
    cout<<"Your Matrix Trace : "<<trace<<endl<<endl;

}
void check_square_matrix(){
    int row=0,col=0;
    cout<<"Enter row and column number of your matrix respectively: ";
    cin>>row>>col;
    if(row == col)
        cout<<"\nIt is a Square Matrix"<<endl<<endl;
    else
        cout<<"\nIt did not match with the condition of  Square Matrix"<<endl<<endl;
}
void check_diagonal_matrix(){
    int r=0,c=0,row=0,col=0,flag=0;
    cout<<"Enter row and column number of your matrix respectively: ";
    cin>>r>>c;
    int mat[r][c]={};
    cout<<"Give Entry/element row-wise: ";


    for(row=0;row<r;row++){
        for(col=0;col<c;col++){
            cin>>mat[r][c];              
        }
    }
    for(row=0;row<r;row++){
        for(col=0;col<c;col++){
            if(row != col){
                if(mat[row][col] != 0){
                    flag=1;
                    break;
                }
                    
            }
                         
        }
        if(flag==1)
            break;
    }
    if(flag==0)
        cout<<"Yesss...It is a Diagonal Matrix"<<endl;
    else
         cout<<"Sorry...It is not Diagonal Matrix"<<endl;

}

void display_list(){
    cout<<"****Here is the LIST********"<<endl;
    cout<<"1 . Determine order of Matrix"<<endl;
    cout<<"2 . Determinne Trace of Matrix"<<endl;
    cout<<"3 . Checking Square Matrix"<<endl;
    cout<<"4 . Checking Diagonal Matrix"<<endl;
    cout<<"5 . Checking Scalar Matrix"<<endl;
    cout<<"6 . Checking Identity/Unit Matrix"<<endl;
    cout<<"7 . Checking Null/Zero Matrix"<<endl;
    cout<<"8 . Checking Triangular Matrix"<<endl;
    cout<<"9 . Checking Transpose Matrix"<<endl;
    cout<<"10 . Checking Symmetric Matrix"<<endl;
    cout<<"11 . Checking Skew Symmetric Matrix"<<endl;
    cout<<"12 . Checking Sub Matrix"<<endl;
    cout<<"13 . Checking Idempotent Matrix"<<endl;
    cout<<"14 . Checking Involutary Matrix"<<endl;
    cout<<"15 . Checking Nilpotent Matrix"<<endl<<endl;
    cout<<"16 . Checking Equality of Matrix"<<endl;
    cout<<"17 . Addition of Matrix"<<endl;
    cout<<"18 . Subtraction of Matrix"<<endl;
    cout<<"19. Multiple of Matrix"<<endl<<endl;
    cout<<"20. Determine Determinant of Matrix"<<endl;
    cout<<"21. Checking given Matrix is Singular or Non-Singular"<<endl;
    cout<<"22 . Determine Inverse Matrix of Given Matrix"<<endl;
    cout<<"23 . Determine Adjoint Matrix of Given Matrix"<<endl<<endl;
    cout<<"69 . Exit "<<endl;

}
void get_selection(int &selection){
    cout<<"Enter your choice : ";
    cin>>selection;
}


int main(){
    int selection {};
    
    
    while(selection !=69 || selection != 69){
        display_list();
        get_selection(selection);

        switch(selection){
            case 1:
                Order_of_matrix();
                break;
            case 2:
                Trace_Matrix();
                break;
            case 3:
                check_square_matrix();
                break;
            case 4:
                check_diagonal_matrix();
                break;
        }

    }
    
    return 0;
}