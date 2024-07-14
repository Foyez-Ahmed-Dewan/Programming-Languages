module encoder (
    input [3:0] Y,
    // output [1:0]A       //use for assign statement
    output reg [1:0]A
);

//using assign statement
/*
assign A[0] = (~Y[3]) & (~Y[2]) & Y[1] | Y[3];
assign A[1] = (~Y[3]) & Y[2] | Y[3];
*/

//using if statement
/*
always @ (*)
    begin
        if (Y[3] == 1'b1) 
            A = 2'b11;
        else if (Y[2] == 1'b1) 
            A = 2'b10;
        else if (Y[1] == 1'b1)
            A = 2'b01;
        else 
            A = 2'b00;
    end
*/

always @ (*)
    begin
        case (1)
            
            //you need to start from backward, otherwise it won't work
            Y[3] : A = 2'b11;
            Y[2] : A = 2'b10;
            Y[1] : A = 2'b01;
            Y[0] : A = 2'b00;
            
            default : A = 2'b00;

        endcase

    end


endmodule