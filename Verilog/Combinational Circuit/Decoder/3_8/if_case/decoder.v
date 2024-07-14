module decoder (
    input E,
    input [2:0] A,
    output reg [7:0] Y   //****output reg where the value is assigned inside always block****
);

//always block using if statement
/*
always @ (*)
    begin

        if (E == 1'b0) 
            Y = 8'b0000_0000;
        else if (A == 3'b000)
            Y = 8'b0000_0001;
        else if (A == 3'b001)
            Y = 8'b0000_0010;
        else if (A == 3'b010)
            Y = 8'b0000_0100;
        else if (A == 3'b011)
            Y = 8'b0000_1000;
        else if (A == 3'b100) 
            Y = 8'b0001_0000;
        else if (A == 3'b101)
            Y = 8'b0010_0000;
        else if (A == 3'b110) 
            Y = 8'b0100_0000;
        else
            Y = 8'b1000_0000;

    end
*/


//always block using case
always @ (*)
    begin
        case ({E, A})


        (4'b1000) : Y = 8'b0000_0001;
        (4'b1001) : Y = 8'b0000_0010;
        (4'b1010) : Y = 8'b0000_0100;
        (4'b1011) : Y = 8'b0000_1000;
        (4'b1100) : Y = 8'b0001_0000;
        (4'b1101) : Y = 8'b0010_0000;
        (4'b1110) : Y = 8'b0100_0000;
        (4'b1111) : Y = 8'b1000_0000;

        default : Y = 8'b0000_0000;

        endcase

    end



endmodule