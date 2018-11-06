`default_nettype none
`timescale 1ns/1ns

/*!
 * Module description.
 */
module top_sync
  // #(
    // parameter _PARAM = DEFAULT_VALUE,
  // )
  (
    // input|inout|output i|io|o_port_name,
    input i_clk,
    input i_reset,
    input i_d,
    output o_q
  );

  // Submodule instantiation
  dff
    // #(
      // ._PARAM(VALUE),
    // )
    u_dff (
      // .i|io|o_port_name(signal|port),
      .i_clk(i_clk),
      .i_reset(i_reset),
      .i_d(i_d),
      .o_q(o_q)
    );

  // Wave dump
  initial begin
    $dumpfile("waves_sync.vcd");
    // $dumpvars(<level>, <module>);
    // level: 0 >> all, 1 >> top only, 2 >> up to 1 level down
    $dumpvars(0, top_sync);
  end

endmodule
