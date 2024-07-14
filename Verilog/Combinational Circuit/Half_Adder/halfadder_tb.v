`timescale  1ns/1ps

module halfadder_tb ();

reg A;
reg B;
wire C;
wire S;

HalfAdder circuit (
    .A (A),
    .B (B),
    .C (C),
    .S (S)
);

// HalfAdder circuit1 (A, B, C, S);

initial begin
    A = 1'b0;
    B = 1'b0;

    #20;
    B = 1'b1;

    #20;

    A = 1'b1;
    B = 1'b0;

    #20;
    B = 1'b1;
    
end

initial begin 
    $monitor ("A = %b, B = %b || C = %b , S = %b", A, B, C, S);
end



endmodule