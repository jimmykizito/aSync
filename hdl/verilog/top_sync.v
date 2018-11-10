`default_nettype none
`timescale 1ns/1ns

/*!
 * Simple synchroniser formed by chaining flip-flops.
 */
module top_sync
  #(
    parameter SYNC_DEPTH = 2
  )
  (
    input i_clk,
    input i_async,
    output o_sync
  );

  sync
    #(
      .SYNC_DEPTH(SYNC_DEPTH)
    )
    u_sync (
      .i_clk(i_clk),
      .i_async(i_async),
      .o_sync(o_sync)
    );

  // Wave dump
  initial begin
    $dumpfile("waves_sync.vcd");
    // $dumpvars(<level>, <module>);
    // level: 0 >> all, 1 >> top only, 2 >> up to 1 level down
    $dumpvars(0, top_sync);
  end

endmodule
