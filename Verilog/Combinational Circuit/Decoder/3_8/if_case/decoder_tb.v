`timescale 1ps/1ps

module decoder_tb();
    reg [2:0] A;
    reg E;
    wire [7:0] Y;

decoder uut (
    .A(A),
    .E(E),
    .Y(Y)
);

initial begin
    E = 1'b0;
    A[0] = 1'b0;
    A[1] = 1'b0;
    A[2] = 1'b0;

    #20;

    E = 1'b1;
    A[0] = 1'b1;

    #20;
    A[0] = 1'b0;
    A[1] = 1'b1;

    #20;
    A[0] = 1'b1;
    A[2] = 1'b1;

end

initial begin 
    $monitor ("E = %b, A2 = %b, A1 = %b, A0 = %b || Y7 = %b, Y6 = %b, Y5 = %b, Y4 = %b, Y3 = %b, Y2 = %b, Y1 = %b, Y0 = %b",
                E, A[2], A[1], A[0], Y[7], Y[6], Y[5], Y[4], Y[3], Y[2], Y[1], Y[0]);
end



endmodule