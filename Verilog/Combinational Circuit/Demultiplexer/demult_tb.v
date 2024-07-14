`timescale 1ns/1ps

module demult_tb ();

reg I;
reg [1:0] S;
wire [3:0] Y;

demultiplexer uut (
    .I (I),
    .S (S),
    .Y (Y)
);

initial begin
    S = 2'b00;
    I = 1'b0;

    #20;
    I = 1'b1;

    #20;
    S = 2'b01;
    
    #20;
    S = 2'b10;

    #20;
    S = 2'b11;
    
end

initial begin
    $monitor ("S1 = %b, S0 = %b, I = %b || Y3 = %b, Y2 = %b, Y1 = %b, Y0 = %b", S[1], S[0], I, Y[3], Y[2], Y[1], Y[0]);
end


endmodule
