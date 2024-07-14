module counter (
    input wire reset,
    input wire clk,
    output wire [6:0] q
);


wire [6:0] d_temp, q_temp;

register register_circuit (reset, clk, d_temp, q_temp);

addOne adder_circuit (q_temp, d_temp);

assign q = q_temp;

endmodule