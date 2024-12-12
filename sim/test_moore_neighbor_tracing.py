import cocotb
import os
import sys
from math import log
import logging
from pathlib import Path
from cocotb.clock import Clock
from cocotb.triggers import Timer, ClockCycles, RisingEdge, FallingEdge, ReadOnly,with_timeout
from cocotb.utils import get_sim_time as gst
from cocotb.runner import get_runner
from make_images import get_image_data


@cocotb.test()
async def test_a(dut):
    """cocotb test for moore_neighbor_tracing"""
    dut._log.info("Starting...")
    cocotb.start_soon(Clock(dut.clk_in, 10, units="ns").start())

    dut.rst_in.value = 0
    dut.x_in.value = 0
    dut.y_in.value = 0
    dut.valid_in.value = 0
    dut.masked_in.value = 0
    dut.new_frame_in.value = 0
    await ClockCycles(dut.clk_in,5)

    dut.rst_in.value = 1
    await ClockCycles(dut.clk_in,5)

    dut.rst_in.value = 0
    

    # wait
    await ClockCycles(dut.clk_in,10000)

    masked_arr = get_image_data("images/square.png")

    # we have a new frame, so add all the pixels
    dut.new_frame_in.value = 1
    for y in range(180):
        for x in range(320):
            await RisingEdge(dut.clk_in)
            dut.x_in.value = x
            dut.y_in.value = y
            dut.valid_in.value = 1
            dut.masked_in.value = masked_arr[y*320 + x]
            dut.new_frame_in.value = 0
            #await RisingEdge(dut.clk_in)
            #dut.valid_in.value = 0
            #await RisingEdge(dut.clk_in)
            #dut._log.info(f"STORING PIXEL: ({x},{y})")

    dut.valid_in.value = 0

    await ClockCycles(dut.clk_in,50000)
    dut._log.info(f"SQUARE PERIMETER: 240 | MOORE COMPUTED PERIMETER: {int(dut.perimeter.value)}")








    # RESET FOR CIRCLE
    dut.rst_in.value = 0
    dut.x_in.value = 0
    dut.y_in.value = 0
    dut.valid_in.value = 0
    dut.masked_in.value = 0
    dut.new_frame_in.value = 0
    await ClockCycles(dut.clk_in,5)

    dut.rst_in.value = 1
    await ClockCycles(dut.clk_in,5)
    dut.rst_in.value = 0

    await ClockCycles(dut.clk_in,10000)

    masked_arr = get_image_data("images/circle.png")


    # we have a new frame, so add all the pixels
    dut.new_frame_in.value = 1
    for y in range(180):
        for x in range(320):
            await RisingEdge(dut.clk_in)
            dut.x_in.value = x
            dut.y_in.value = y
            dut.valid_in.value = 1
            dut.masked_in.value = masked_arr[y*320 + x]
            dut.new_frame_in.value = 0
            #await RisingEdge(dut.clk_in)
            #dut.valid_in.value = 0
            #await RisingEdge(dut.clk_in)
            #dut._log.info(f"STORING PIXEL: ({x},{y})")

    dut.valid_in.value = 0

    await ClockCycles(dut.clk_in,50000)
    dut._log.info(f"CIRCLE PERIMETER: 168 | MOORE COMPUTED PERIMETER: {int(dut.perimeter.value)}")









    # RESET FOR TRIANGLE
    dut.rst_in.value = 0
    dut.x_in.value = 0
    dut.y_in.value = 0
    dut.valid_in.value = 0
    dut.masked_in.value = 0
    dut.new_frame_in.value = 0
    await ClockCycles(dut.clk_in,5)

    dut.rst_in.value = 1
    await ClockCycles(dut.clk_in,5)
    dut.rst_in.value = 0

    await ClockCycles(dut.clk_in,10000)

    masked_arr = get_image_data("images/triangle.png")


    # we have a new frame, so add all the pixels
    dut.new_frame_in.value = 1
    for y in range(180):
        for x in range(320):
            await RisingEdge(dut.clk_in)
            dut.x_in.value = x
            dut.y_in.value = y
            dut.valid_in.value = 1
            dut.masked_in.value = masked_arr[y*320 + x]
            dut.new_frame_in.value = 0
            #await RisingEdge(dut.clk_in)
            #dut.valid_in.value = 0
            #await RisingEdge(dut.clk_in)
            #dut._log.info(f"STORING PIXEL: ({x},{y})")

    dut.valid_in.value = 0

    await ClockCycles(dut.clk_in,50000)
    dut._log.info(f"TRIANGLE PERIMETER: 179 | MOORE COMPUTED PERIMETER: {int(dut.perimeter.value)}") # Moore outputs 180 on triangle. this happens because of the width-1 section in the triangle, causing it to double count one of the pixels







    # RESET FOR PLUS
    dut.rst_in.value = 0
    dut.x_in.value = 0
    dut.y_in.value = 0
    dut.valid_in.value = 0
    dut.masked_in.value = 0
    dut.new_frame_in.value = 0
    await ClockCycles(dut.clk_in,5)

    dut.rst_in.value = 1
    await ClockCycles(dut.clk_in,5)
    dut.rst_in.value = 0

    await ClockCycles(dut.clk_in,10000)

    masked_arr = get_image_data("images/plus.png")


    # we have a new frame, so add all the pixels
    dut.new_frame_in.value = 1
    for y in range(180):
        for x in range(320):
            await RisingEdge(dut.clk_in)
            dut.x_in.value = x
            dut.y_in.value = y
            dut.valid_in.value = 1
            dut.masked_in.value = masked_arr[y*320 + x]
            dut.new_frame_in.value = 0
            #await RisingEdge(dut.clk_in)
            #dut.valid_in.value = 0
            #await RisingEdge(dut.clk_in)
            #dut._log.info(f"STORING PIXEL: ({x},{y})")

    dut.valid_in.value = 0


    await ClockCycles(dut.clk_in,50000)
    dut._log.info(f"PLUS PERIMETER: 396 | MOORE COMPUTED PERIMETER: {int(dut.perimeter.value)}")


    





def is_runner():
    """Image Sprite Tester."""
    hdl_toplevel_lang = os.getenv("HDL_TOPLEVEL_LANG", "verilog")
    sim = os.getenv("SIM", "icarus")
    proj_path = Path(__file__).resolve().parent.parent
    sys.path.append(str(proj_path / "sim" / "model"))
    sources = [proj_path / "hdl" / "moore_neighbor_tracing.sv"]
    #sources += [proj_path / "ip" / "blk_mem_gen_0" / "blk_mem_gen_0.xci"]
    sources += [proj_path / "hdl" / "xilinx_true_dual_port_read_first_2_clock_ram.v"]
    build_test_args = ["-Wall"]
    parameters = {}
    sys.path.append(str(proj_path / "sim"))
    runner = get_runner(sim)
    runner.build(
        sources=sources,
        hdl_toplevel="moore_neighbor_tracing",
        always=True,
        build_args=build_test_args,
        parameters=parameters,
        timescale = ('1ns','1ps'),
        waves=True
    )
    run_test_args = []
    runner.test(
        hdl_toplevel="moore_neighbor_tracing",
        test_module="test_moore_neighbor_tracing",
        test_args=run_test_args,
        waves=True
    )

if __name__ == "__main__":
    is_runner()
