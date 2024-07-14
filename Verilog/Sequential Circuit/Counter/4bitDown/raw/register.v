module register (
    input wire reset,
    input wire clk,
    input wire [3:0] d,
    output reg [3:0] q
);

always @ (posedge reset, posedge clk)
    begin
        
        if (reset)
            q <= 4'b0000;
        else 
            q <= d;

    end

endmodule