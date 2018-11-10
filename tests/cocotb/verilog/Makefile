TOPLEVEL_LANG=verilog

SIM?=icarus
# add -P$(TOPLEVEL).SYNC_DEPTH=$(SYNC_DEPTH) to SIM_ARGS from ../test.mk

PWD=$(shell pwd)
COCOTB?=/usr/local/src/cocotb.git
PYTHONPATH:=$(PWD)/../:$(PYTHONPATH)

# Top level source
VERILOG_SOURCES=$(PWD)/../../../hdl/verilog/top_sync.v
# Submodule sources
VERILOG_SOURCES+=$(PWD)/../../../hdl/verilog/sync.v
TOPLEVEL=top_sync

MODULE=test_sync

include $(COCOTB)/makefiles/Makefile.inc
include $(COCOTB)/makefiles/Makefile.sim
