import random

import cocotb
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue

import sync
from sync.sync_tb import SyncTestbench

@cocotb.test()
def test_sync(dut):
    """
    Test D-type flip-flop (DFF) with asynchronous reset.
    """

    sim_units = "ns" # simulator timing resolution
    clk_period = 20e-9 # 50 MHz clock

    tb = SyncTestbench(dut)

    # Assert reset then toggle DFF inputs at random intervals.
    tb.drv.start_clk(clk_period)
    dut.i_d <= 0
    yield tb.drv.reset(2 * clk_period)

    reset_thd = cocotb.fork(
        tb.drv.randomise_bit(dut.i_reset, 1, 10, 500, sim_units))
    d_thd = cocotb.fork(
        tb.drv.randomise_bit(dut.i_d, 10, 100, 1000, sim_units))

    yield reset_thd.join()
    dut.i_reset <= 0
    yield d_thd.join()

    raise tb.sb.result
