module sample (
    input [1:0] S,
    input [4:0] A,
    input [4:0] B,
    output reg [4:0] Y
);

always @ (*) 
    begin
        if (S == 2'b11) 
            Y = A | B;
        else if (S == 2'b10)
            Y = A << B;
        else if (S == 2'b01)
            Y = A >> B;
        else 
            Y = B;
    
    end


endmodule