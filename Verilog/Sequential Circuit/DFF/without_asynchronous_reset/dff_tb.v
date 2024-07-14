`timescale 1ns/1ps

module dff_tb ();

reg d;
reg clk;
wire q;

dff circuit (d, clk, q);

always begin
    clk = ~clk;
    #10;
end

initial begin 
    clk <= 1'b0;
    d <= 1'b0;

    #20;
    d <= 1'b1;
    #20;

    $finish;

end

initial begin
    $monitor ("CLK = %b, d = %b || q = %b", clk, d, q);
end


endmodule