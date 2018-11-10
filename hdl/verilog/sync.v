`default_nettype none
`timescale 1ns/1ns

module sync
  #(
    parameter SYNC_DEPTH = 2
  )
  (
    input i_clk,
    input i_async,
    output o_sync
  );

  logic [SYNC_DEPTH - 1: 0] sync_shift_reg = 'b0;

  assign o_sync = sync_shift_reg[SYNC_DEPTH - 1];

  always @(posedge i_clk)
      sync_shift_reg <= {sync_shift_reg[SYNC_DEPTH - 2: 0], i_async};

endmodule
