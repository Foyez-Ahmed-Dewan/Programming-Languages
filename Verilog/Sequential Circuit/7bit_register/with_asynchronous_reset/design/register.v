module register (
    input wire reset,
    input wire clk,
    input wire [6:0] d,
    output reg [6:0] q
);

//signal declaration
reg [6:0] q_next;
reg [6:0] q_reg;

//memory 
always @ (posedge reset, posedge clk)
    begin
        if (reset)
            q_reg <= 7'b0000_000;
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