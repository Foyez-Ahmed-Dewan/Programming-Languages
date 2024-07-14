`timescale 1ns/1ps

module register_tb ();

reg reset;
reg clk;
reg en;
reg [6:0] d;
wire [6:0] q;

register cicuit (reset, clk, en, d, q);

always begin
    clk = ~clk;
    #10;
end


initial begin 
    reset <= 1;
    clk <= 0;
    d <= 7'b0000_000;
    en <= 0;

    #20;
    reset <= 0;
    d <= 7'b0000_111;
    en <= 1;
    #20;

    $finish;

end

initial begin
    $monitor ("reset = %b, clk = %b, en = %b, d = %b || q = %b", reset, clk, en, d, q);
end

endmodule



