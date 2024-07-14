`timescale 1ns/1ps

module multiplexer_tb ();

reg [1:0] S;
reg [3:0] I;
wire Y;

multiplexer uut (
    .S (S),
    .I (I),
    .Y (Y)
);

initial begin
    S = 2'b00;
    I = 4'b0000;

    #20;
    I[0] = 1'b1;

    #20;
    S = 2'b01;
    I = 4'b0000;
    
    #20;
    I[1] = 1'b1;

    #20;
    S = 2'b11;
    I[3] = 1'b1;
    I[0] = 1'b0;


end

initial begin 
    $monitor ("S1 = %b, S0 = %b, I3 = %b, I2 = %b, I1 = %b, I0 = %b || Y = %b", S[1], S[0], I[3], I[2], I[1], I[0], Y);

end



endmodule