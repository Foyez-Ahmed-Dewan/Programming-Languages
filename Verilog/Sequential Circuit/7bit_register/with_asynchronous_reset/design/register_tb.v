`timescale 1ns/1ps

module register_tb ();

reg reset;
reg clk;
reg [6:0] d;
wire [6:0]q;

register circuit (reset, clk, d, q);

always begin
    clk = ~clk;
    #10;
end


initial begin
    clk <= 0;
    reset <= 1;
    d <= 7'b0000_000;

    #20;
    reset <= 0;
    d <= 7'b0000_111;
    #20;

    $finish;
    
end


initial begin
    $monitor ("reset = %b, clk = %b, d = %b || q = %b", reset, clk, d, q);

end


endmodule