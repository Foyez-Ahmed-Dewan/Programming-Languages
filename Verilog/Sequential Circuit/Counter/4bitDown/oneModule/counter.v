module counter (
    input wire reset,
    input wire clk,
    output wire [3:0] q
);

wire [3:0] d_temp;
reg [3:0] q_temp;

//state register
always @ (posedge reset, posedge clk) 
begin
    if (reset)
        q_temp <= 4'b0000;
    else 
        q_temp <= d_temp;    
end

//next state logic
assign d_temp = q_temp - 1;

//output logic
assign q = q_temp;

endmodule