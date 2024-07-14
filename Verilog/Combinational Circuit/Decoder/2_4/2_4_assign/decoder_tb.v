`timescale 1ps/1ps

module decoder_tb ();

reg [1:0]A;
reg E;
wire [3:0]Y;

decoder uut (
    .A (A),
    .E (E),
    .Y (Y)
);

initial begin
    $dumpfile("test.vcd");
    $dumpvars(0, decoder_tb);
    
    A[1] = 1'b0;
    A[0] = 1'b1;
    E = 1'b0;

    #20;
    E = 1'b1;

    #20;
    A[0] = 1'b0;

    #20;
    A[1] = 1'b1;

    #20;
    A[0] = 1'b1;

end


initial begin 
    $monitor ("E = %b, A1 = %b, A0 = %b || Y3 = %b, Y2 = %b, Y1 = %b, Y0 = %b", E, A[1], A[0], Y[3], Y[2], Y[1], Y[0]);
end




endmodule