module register (
    input wire reset,
    input wire clk,
    input wire [3:0] d,
    output reg [3:0] q
);

//signal declaration
reg [3:0] q_reg, q_next;

//memory
always @ (posedge reset, posedge clk)
    begin
        if (reset) 
            q_reg <= 4'b0000;
        else 
            q_reg <= q_next;
    end


//next state logic
always @ (*)
    begin
        q_next <= d;
    end

//output logic
always @ (*)
    begin
        q <= q_reg;
    end


endmodule