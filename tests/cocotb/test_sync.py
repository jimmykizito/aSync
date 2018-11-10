import random

import cocotb
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue

import sync
from sync.sync_tb import SyncTestbench

@cocotb.test()
def test_sync(dut):
    """
    Test synchroniser with random length asynchronous pulses.
    """

    sim_units = "ns" # simulator timing resolution
    clk_period = 20e-9 # 50 MHz clock

    tb = SyncTestbench(dut)

    # Clear asynchronous input, then toggle randomly
    dut.i_async <= 0
    tb.drv.start_clk(clk_period)

    yield tb.drv.randomise_bit(dut.i_async, 1, 100, 1000, sim_units)

    raise tb.sb.result
