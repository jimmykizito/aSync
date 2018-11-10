import collections
from collections import deque

import cocotb
from cocotb.binary import BinaryValue

class SyncModel(object):

    def __init__(self, dut, **kwargs):
        self.dut = dut
        self.exp_out = kwargs.get("exp_out")
        sync_depth = int(dut.SYNC_DEPTH)
        self._sync_shift_reg = deque([BinaryValue(0)] * sync_depth, sync_depth)

    def callback(self, transaction):
        """
        Shift asynchronous input into shift register on rising clock edge.
        """
        self._sync_shift_reg.append(transaction)
        self.exp_out.append(self._sync_shift_reg[0])
