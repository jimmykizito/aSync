import cocotb

from sync.sync_drv import SyncDriver
from sync.sync_mdl import SyncModel
from sync.sync_mon import SyncMonitorIn, SyncMonitorOut
from sync.sync_sb import SyncScoreBoard

class SyncTestbench:
    """
    Houses cocotb test components.

    - Monitor captures simulation input and output.
    - Model uses captured input to produce expected output from Python model of
    DUT.
    - Scoreboard compares captured output from simulation to expected output
    model.
    """

    def __init__(self, dut, **kwargs):
        self.dut = dut
        #self.attr = kwargs.get("name of arg")

        self.exp_out = []
        self._mdl = SyncModel(self.dut, exp_out=self.exp_out)

        self._mon_in = SyncMonitorIn(self.dut, "sync_in",
                                     callback=self._mdl.callback)

        self._mon_out = SyncMonitorOut(self.dut, "sync_out")

        self.sb = SyncScoreBoard(self.dut)
        self.sb.add_interface(self._mon_out, self.exp_out)

        self.drv = SyncDriver(self.dut)
