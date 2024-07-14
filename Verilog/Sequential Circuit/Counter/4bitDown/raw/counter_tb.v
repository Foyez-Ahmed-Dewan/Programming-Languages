`timescale 1ns/1ps

module counter_tb ();

reg reset;
reg clk;
wire [3:0] q;

counter circuit (reset, clk, q);

always begin
    clk = ~clk;
    #10;
end

initial begin
    reset <= 1;
    clk <= 0;

    #20;
    reset <= 0;

    #20;
    #20;
    #20;
    #20;

    $finish;




end


initial begin
    $monitor ("reset = %b, clk = %b, q = %b", reset, clk, q);
end



endmodule