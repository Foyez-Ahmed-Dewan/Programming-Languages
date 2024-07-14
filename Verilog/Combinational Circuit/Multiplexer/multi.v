module multiplexer (
    input [1:0] S,
    input [3:0] I,
    // output Y //use this if you're using assign statement
    output reg Y
);
//using assign statement
// assign Y = (~S[1]) & (~S[0]) & I[0] |(~S[1]) & (S[0]) & I[1] | (S[1]) & (~S[0]) & I[2] | (S[1]) & (S[0]) & I[3];

//using if statement
/*
always @ (*) 
    begin
        if (S == 2'b00)
            Y = I[0];
        else if (S == 2'b01)
            Y = I[1];
        else if (S == 2'b10)
            Y = I[2];
        else 
            Y = I[3];

    end

*/


//using case statement
always @ (*) 
    begin
        case (S)

            (2'b00) : Y = I[0];
            (2'b01) : Y = I[1];
            (2'b10) : Y = I[2];
            (2'b11) : Y = I[3];

            default : Y = 1'b0;

        endcase


    end

endmodule