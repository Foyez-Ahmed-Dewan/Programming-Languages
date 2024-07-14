`timescale 1ns/1ps

module encoder_tb();

reg [3:0] Y;
wire [1:0] A;

encoder uut (
    .Y (Y),
    .A (A)
);


initial begin
    Y[3] = 1'b0; 
    Y[2] = 1'b0; 
    Y[1] = 1'b0; 
    Y[0] = 1'b1; 

    #20;
    Y[1] = 1'b1; 
    Y[0] = 1'b0; 

    #20;
    Y[2] = 1'b1; 
    Y[1] = 1'b0; 

    #20;

    Y[3] = 1'b1; 
    Y[2] = 1'b0; 

    #20;
    Y[3] = 1'b1;
    Y[2] = 1'b0;
    Y[1] = 1'b1;
    Y[0] = 1'b0;

end


initial begin 
    $monitor ("Y3 = %b, Y2 = %b, Y1 = %b, Y0 = %b || A1 = %b, A0 = %b", Y[3], Y[2], Y[1], Y[0], A[1], A[0]);
end 

endmodule