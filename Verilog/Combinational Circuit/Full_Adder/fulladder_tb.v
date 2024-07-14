`timescale 1ns/1ps
// first indicates how much time to wait? second indicates zooming ratio

module Adder1bit_tb
(
);

// input as register, output as wire
// this name can be different from input name
reg A;
reg B;
reg Cin;
wire S;
wire Co;

Adder1bit circuit1  
(
    .A (A),
    .B (B),
    .Cin (Cin),
    .Co (Co),
    .S (S)
);


//x'by -> x = koto biter output? y = value koto?
initial begin
    //this two line is used to show the result 
    $dumpfile ("output.vcd");
    $dumpvars(0, Adder1bit_tb);

    A = 1'b0;  
    B = 1'b1;
    Cin = 1'b1;  

    #20;  //for 20ns, this value will remain same

    B = 1'b0;
    #20

    $finish;
end

initial begin
    $monitor ("A = %b B = %b Cin = %b || Cout = %b S = %b\n", A, B, Cin, Co, S);
end

endmodule