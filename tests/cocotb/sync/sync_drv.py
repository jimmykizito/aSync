import random

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.result import ReturnValue

class SyncDriver(object):

    def __init__(self, dut):
        self.dut = dut

    def start_clk(self, clk_period):
        cocotb.fork(Clock(self.dut.i_clk, clk_period, units='sec').start())

    @cocotb.coroutine
    def reset(self, duration, units='sec', is_hi=True):
        if is_hi:
            reset_val = 1
        else:
            reset_val = 0
        self.dut.i_reset <= reset_val
        yield Timer(duration, units=units)
        self.dut.i_reset <= reset_val ^ 1

    @cocotb.coroutine
    def _delay(self, duration, units='sec'):
        # Wrap Timer() in coroutine to allow forking.
        yield Timer(duration, units=units)
        raise ReturnValue(duration) # change to return dur for Python3

    @cocotb.coroutine
    def randomise_bit(self, signal, t_min, t_max, timeout, units='sec'):
        """
        Toggle signal at random intervals in range [t_min, t_max] until
        'timeout' units of time have passed.
        """
        to_thd = cocotb.fork(self._delay(timeout, units))
        to = to_thd.join()
        while True:
            t_delay = random.randint(t_min, t_max)
            trigger = yield [Timer(t_delay, units=units), to]
            if trigger == timeout:
                break
            signal <= int(~signal.value)
