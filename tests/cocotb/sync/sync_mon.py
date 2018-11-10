import cocotb
from cocotb.monitors import Monitor
from cocotb.triggers import RisingEdge, ReadOnly

class SyncMonitorIn(Monitor):

    def __init__(self, dut, name, callback=None, **kwargs):
        self.dut = dut
        self.name = name
        Monitor.__init__(self, callback=callback)

    def __str__(self):
        return "%s(%s)" % (self.__class__.__name__, self.name)

    @cocotb.coroutine
    def _monitor_recv(self):
        clk_edge = RisingEdge(self.dut.i_clk)
        ro = ReadOnly()

        while True:
            yield clk_edge
            yield ro

            transaction = self.dut.i_async.value

            self._recv(transaction)

class SyncMonitorOut(Monitor):

    def __init__(self, dut, name, **kwargs):
        self.dut = dut
        self.name = name
        Monitor.__init__(self)

    def __str__(self):
        return "%s(%s)" % (self.__class__.__name__, self.name)

    @cocotb.coroutine
    def _monitor_recv(self):
        clk_edge = RisingEdge(self.dut.i_clk)
        ro = ReadOnly()

        while True:
            yield clk_edge
            yield ro

            self._recv(self.dut.o_sync.value)
