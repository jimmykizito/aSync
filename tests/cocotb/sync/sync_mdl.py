import cocotb
from cocotb.binary import BinaryValue

class SyncModel(object):

    def __init__(self, dut, **kwargs):
        self.dut = dut
        self.exp_out = kwargs.get("exp_out")
        self._clk_prev = BinaryValue(1)
        self._q_current = BinaryValue(0)

    def callback(self, transaction):
        """
        Use string representation for comparisons since X and Z resolve to
        error values when BinaryValue treated numerically.
        """
        if transaction.reset_val.get_binstr() is "1":
            self._q_current = BinaryValue(0)
        elif self._clk_prev.get_binstr() is "0" and \
             transaction.clk_val.get_binstr() is "1":
            self._q_current = transaction.d_val
        self._clk_prev = transaction.clk_val
        self.exp_out.append(self._q_current)

class SyncTransaction(object):

    def __init__(self, reset_val=None, clk_val=None, d_val=None):
        self.reset_val = reset_val
        self.clk_val = clk_val
        self.d_val = d_val
