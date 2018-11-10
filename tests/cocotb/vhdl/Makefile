TOPLEVEL_LANG=vhdl

SIM?=ghdl
SIM_ARGS?="--wave=waves_sync.ghw"
# add -gPARAM=VAL to SIM_ARGS from ../test.mk

PWD=$(shell pwd)
COCOTB?=/usr/local/src/cocotb.git
PYTHONPATH:=$(PWD)/../:$(PYTHONPATH)

# Top-level source
VHDL_SOURCES=$(PWD)/../../../hdl/vhdl/top_sync.vhd
# Submodule sources
VHDL_SOURCES+=$(PWD)/../../../hdl/vhdl/sync.vhd
TOPLEVEL=top_sync

MODULE=test_sync

include $(COCOTB)/makefiles/Makefile.inc
include $(COCOTB)/makefiles/Makefile.sim
