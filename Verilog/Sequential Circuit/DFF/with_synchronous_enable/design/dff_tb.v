`timescale 1ns/1ps

module dff_tb ();

reg d;
reg clk;
reg reset;
reg en;
wire q;

dff circuit (reset, clk, en, d, q);

always begin

    clk = ~clk;
    #10;

end

initial begin 
    reset <= 1;
    d <= 0;
    en <= 0;
    clk <= 0;

    #20;
    reset <= 0;
    en <= 1;
    d <= 1;

    #20;

    $finish;

end

initial begin 
    $monitor ("reset = %b, en = %b, clk = %b, d = %b || q = %b", reset, en, clk, d, q);
end 

endmodule