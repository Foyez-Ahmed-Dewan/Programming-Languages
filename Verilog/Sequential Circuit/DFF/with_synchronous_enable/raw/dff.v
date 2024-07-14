module dff (
    input wire d,
    input wire clk,
    input wire reset,
    input wire en,
    output reg q
); 

always @ (posedge reset, posedge clk) 
    begin
       
        if (reset) 
            q <= 0;
        else if (en)
            q <= d;
    end

endmodule