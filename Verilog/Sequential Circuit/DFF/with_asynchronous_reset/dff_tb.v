`timescale 1ns/1ps

module dff_tb ();

reg clk;
reg reset;
reg d;
wire q;

dff circuit (clk, d, reset, q);

always begin
    clk = ~clk;
    #10;
end


initial begin
    clk <= 0;
    reset <= 1;
    d <= 0;

    #20;
    reset <= 1'b0;
    d <= 1;
    #20;

    $finish;

end


initial begin
    $monitor ("Reset = %b, clk = %b, d = %b || q = %b", reset, clk, d, q);
end

endmodule