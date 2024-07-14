module dff (
    input wire clk,
    input wire d,
    input wire reset,
    output reg q
);

always @ (posedge reset, posedge clk)
    begin
        if (reset) 
            q <= 0;
        else 
            q <= d;
    
    end


endmodule