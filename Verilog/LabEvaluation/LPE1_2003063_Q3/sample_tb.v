`timescale 1ns/1ps

module sample_tb ();

reg [1:0] S;
reg [4:0] A;
reg [4:0] B;
wire [4:0] Y;

sample uut (
    .S (S),
    .A (A),
    .B (B),
    .Y (Y)
);

initial begin
    A = 5'b00101;
    B = 5'b01010;

    S = 2'b00;

    #20;

    S = 2'b01;

    #20;

    S = 2'b10;

    #20;

    S = 2'b11;

end

initial begin
    $monitor ("S = %b, A = %b, B = %b || Y = %b", S, A, B, Y);
end

endmodule