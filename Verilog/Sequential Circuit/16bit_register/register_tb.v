`timescale 1ns/1ps

module register_tb ();

reg reset;
reg clk;
reg [15:0] d;
wire [15:0] q;

register circuit (reset, clk, d, q);

always begin
    clk = ~clk;
    #10;
end

initial begin
    clk <= 0;
    d <= 16'b0000_0000_0000_0000;
    reset <= 1;

    #20;
    reset <= 0;
    d <= 16'b0000_0000_0000_1111;

    #20;

    $finish;

end

initial begin
    $monitor ("reset = %b, clk = %b, d = %b, q = %b", reset, clk, d, q);
end


endmodule