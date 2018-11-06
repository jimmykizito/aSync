TOPLEVEL_LANG=verilog

SIM?=icarus

PWD=$(shell pwd)
COCOTB?=/usr/local/src/cocotb.git
PYTHONPATH:=$(PWD)/../:$(PYTHONPATH)

# Top level source
VERILOG_SOURCES=$(PWD)/../../../hdl/verilog/top_sync.v
# Submodule sources
VERILOG_SOURCES+=$(PWD)/../../../hdl/verilog/dff.v
TOPLEVEL=top_sync

MODULE=test_sync

include $(COCOTB)/makefiles/Makefile.inc
include $(COCOTB)/makefiles/Makefile.sim
