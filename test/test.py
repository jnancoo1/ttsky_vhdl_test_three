# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1

    # Full adder truth table tests
for i in range(8):

    dut.ui_in.value = i
    await ClockCycles(dut.clk, 1)

    A = (i >> 0) & 1
    B = (i >> 1) & 1
    C = (i >> 2) & 1

    SUM = A ^ B ^ C
    CARRY = (A & B) | ((A ^ B) & C)

    expected = (SUM << 1) | CARRY

    dut._log.info(f"A={A} B={B} C={C} expected={expected}")

    assert (dut.uo_out.value.integer & 0b11) == expected
