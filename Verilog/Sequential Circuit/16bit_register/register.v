module register (
    input wire reset,
    input wire clk,
    input wire [15:0] d,
    output reg [15:0] q
);

always @ (posedge reset, posedge clk)
    begin
        if (reset)
            q <= 16'b0000_0000_0000_0000;
        else 
            q <= d;
    end

endmodule