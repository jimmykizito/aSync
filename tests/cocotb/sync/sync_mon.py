import cocotb
from cocotb.monitors import Monitor
from cocotb.triggers import Edge, RisingEdge, ReadOnly

from sync.sync_mdl import SyncTransaction

class SyncMonitorIn(Monitor):

    def __init__(self, dut, name, callback=None, **kwargs):
        self.dut = dut
        self.name = name
        Monitor.__init__(self, callback=callback)

    def __str__(self):
        return "%s(%s)" % (self.__class__.__name__, self.name)

    @cocotb.coroutine
    def _monitor_recv(self):
        reset_edge = Edge(self.dut.i_reset)
        d_edge = Edge(self.dut.i_d)
        clk_edge = Edge(self.dut.i_clk)
        transaction = SyncTransaction()
        ro = ReadOnly()

        while True:
            yield [reset_edge, clk_edge, d_edge]
            yield ro

            transaction.reset_val = self.dut.i_reset.value
            transaction.clk_val = self.dut.i_clk.value
            transaction.d_val = self.dut.i_d.value

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
        reset_edge = Edge(self.dut.i_reset)
        d_edge = Edge(self.dut.i_d)
        clk_edge = Edge(self.dut.i_clk)
        ro = ReadOnly()

        while True:
            yield [reset_edge, clk_edge, d_edge]
            yield ro

            self._recv(self.dut.o_q.value)
