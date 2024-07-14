module encoder (
    input [3:0]Y,
    output [1:0]A //during assign
    // output reg [1:0]A //during if or case
);

//using assign statement
// /*
assign A[1] = Y[2] | Y[3];
assign A[0] = Y[1] | Y[3];
// */

//using if statement
/*
always @ (*) 
begin
    if (Y == 4'b0001)
        A = 2'b00;
    else if (Y == 4'b0010)
        A = 2'b01;
    else if (Y == 4'b0100)
        A = 2'b10;
    else 
        A = 2'b11;
    
end
*/

//using case statement
// always @ (*)
//     begin
//         case (Y)
//             (4'b0001) : A = 2'b00;
//             (4'b0010) : A = 2'b01;
//             (4'b0100) : A = 2'b10;
//             (4'b1000) : A = 2'b11;
//         endcase
//     end



endmodule