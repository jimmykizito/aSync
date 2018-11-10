import random

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.result import ReturnValue

class SyncDriver(object):

    def __init__(self, dut):
        self.dut = dut

    def start_clk(self, clk_period):
        cocotb.fork(Clock(self.dut.i_clk, clk_period, units="sec").start())

    @cocotb.coroutine
    def _delay(self, duration, units="sec"):
        # Wrap Timer() in coroutine to allow forking.
        yield Timer(duration, units=units)
        raise ReturnValue(duration) # change to return dur for Python3

    @cocotb.coroutine
    def randomise_bit(self, signal, t_min, t_max, t_total, units="sec"):
        """
        Toggle signal at random intervals in range [t_min, t_max] until
        't_total' units of time have passed.
        """
        timeout_thd = cocotb.fork(self._delay(t_total, units))
        timeout = timeout_thd.join()
        while True:
            t_delay = random.randint(t_min, t_max)
            t_elapsed = yield [Timer(t_delay, units=units), timeout]
            if t_elapsed == t_total:
                break
            signal <= int(~signal.value)
