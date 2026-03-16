import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    dut.rst_n.value = 0
    dut.ena.value = 1
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    # A=1 B=1 Cin=0
    dut.ui_in.value = 0b00000011
    await ClockCycles(dut.clk, 1)

    # sum=0 carry=1 -> 00000001
    assert dut.uo_out.value.integer == 1
