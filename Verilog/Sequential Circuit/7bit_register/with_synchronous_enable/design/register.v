module register (
    input wire reset,
    input wire clk,
    input wire en,
    input wire [6:0] d,
    output reg [6:0] q
);

//signal declaration
reg [6:0] q_reg;
reg [6:0] q_next;

//memory
always @ (posedge reset, posedge clk) 
    begin
        if (reset)
            q_reg <= 7'b0000_000;
        else if (en)
            q_reg <= q_next;
    end

//next state logic
always @ (*)
begin
    if (en)
        q_next <= d;
    else 
        q_next <= q_reg;
end


//output
always @ (*)
begin
    q <= q_reg;

end


endmodule