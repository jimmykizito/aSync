aSync
=====

A simple synchroniser formed by a chain of flip-flops to reduce the effects of
metastability.

Directory structure:
```
<root_dir>
|-- build
|-- docs
|-- hdl                     # HDL source files
    |-- verilog
    |-- vhdl
|-- include
|-- lib
|-- proj
|-- README.md
|-- sw
|-- tests                   # Test source files
    |-- cocotb
        |-- sync        # Python module for Cocotb tests
        |-- verilog
        |-- vhdl
|-- tools
```

Usage
-----

```
cd test/cocotb/<verilog|vhdl>
make clean
make
gtkwave [sim_build/]waves_tut_sync_logic.[vcd/ghw]
```

Dependencies
------------
- icarus
- ghdl
- gtkwave
