module Adder1bit
(
    // ports here
    input A,
    input B,
    input Cin,
    output Co,
    output S
);

// expression
assign S = A ^ B ^ Cin;
assign Co = (A & B) | ((A ^ B) & Cin);

endmodule

// for testing, we need to write test bench code