`default_nettype none
`timescale 1ns/1ns

module dff
  (
    input i_clk,
    input i_reset,
    input i_d,
    output logic o_q
  );

  always @(posedge i_clk, posedge i_reset) begin
    if (i_reset)
      o_q <= 1'b0;
    else
      o_q <= i_d;
  end

endmodule
