module demultiplexer (
    input I,
    input [1:0] S,
    // output [3:0] Y  //use this only if using assign statement
    output reg [3:0] Y
);

//using assign statement
/*

assign Y[0] = (~S[1]) & (~S[0]) & I;
assign Y[1] = (~S[1]) & (S[0]) & I;
assign Y[2] = (S[1]) & (~S[0]) & I;
assign Y[3] = (S[1]) & (S[0]) & I;

*/

//using if statement 
/*

always @ (*) 
    begin 
        Y = 4'b0000;    // very important, we need to reset it to remove previous output

        if (S == 2'b00)
            Y[0] = I;
        else if (S == 2'b01)
            Y[1] = I;
        else if (S == 2'b10)
            Y[2] = I;
        else 
            Y[3] = I;
    end

*/

always @ (*)
    begin
        case (S)

        (2'b00) : Y[0] = I;
        (2'b01) : Y[1] = I;
        (2'b10) : Y[2] = I;
        (2'b11) : Y[3] = I;

        endcase


    end

endmodule