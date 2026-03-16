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
