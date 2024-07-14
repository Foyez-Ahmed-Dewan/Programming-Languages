module register (
    input wire reset,
    input wire clk,
    input wire en,
    input wire [6:0] d,
    output reg [6:0] q
);

always @ (posedge reset, posedge clk)
    begin
        if (reset)
            q <= 7'b0000_000;
        else if (en)
            q <= d;

    end


endmodule