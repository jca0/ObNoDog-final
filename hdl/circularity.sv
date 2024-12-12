`timescale 1ns / 1ps
`default_nettype none


module circularity (
    input wire clk_in,
    input wire rst_in,
    input wire [$clog2(WIDTH*HEIGHT):0] area,
    input wire [$clog2(WIDTH*HEIGHT):0] perimeter,
    input wire data_valid_in,
    
    output logic [$clog2(WIDTH*HEIGHT):0] circularity,
    output logic busy_out,
    output logic valid_out
    );

    parameter HEIGHT = 320; // changable parameter for height and width of screen
    parameter WIDTH = 180;

    //logic [$clog2(WIDTH*HEIGHT)+4:0] dividend;
    //logic [$clog2(WIDTH*HEIGHT)*2:0] divisor;
    logic [31:0] dividend;
    logic [31:0] divisor;

    logic [31:0] div_quotient; // outputs of divider
    logic [31:0] div_remainder;
    logic div_data_valid_out;
    logic div_error_out;
    logic div_busy_out;

    // always_comb begin
    //     if(rst_in) begin
    //         valid_out = 0;
    //         circularity = 0;
    //         busy_out = 0;

    //     end else begin
    //         dividend = 4 * area * 314; // pi = 3.14 * 100 (so we get an integer 0-100)
    //         divisor = perimeter * perimeter;

    //         valid_out = div_data_valid_out;
    //         circularity = div_quotient;
    //         busy_out = div_busy_out;
    //     end
    // end

    always_ff @(posedge clk_in) begin
        if (rst_in) begin
            dividend <= 0;
            divisor <= 0;
            div_quotient <= 0;
            div_remainder <= 0;
            div_data_valid_out <= 0;
            div_error_out <= 0;
            div_busy_out <= 0;
            busy_out <= 0;
            valid_out <= 0;
            circularity <= 0;
        end else begin
            dividend <= 4 * area * 314; // pi = 3.14 * 100 (so we get an integer 0-100)
            divisor <= perimeter * perimeter;

            div_quotient <= div_quotient;
            div_remainder <= div_remainder;
            div_data_valid_out <= div_data_valid_out;
            div_error_out <= div_error_out;
            div_busy_out <= div_busy_out;
            busy_out <= div_busy_out;
            valid_out <= div_data_valid_out;
            circularity <= div_quotient;
        end
    end

    divider
    #(.WIDTH(64)
    ) my_divider
    (.clk_in(clk_in),
        .rst_in(rst_in),
        .dividend_in(dividend),
        .divisor_in(divisor),
        .data_valid_in(data_valid_in),
        .quotient_out(div_quotient), // outputs
        .remainder_out(div_remainder),
        .data_valid_out(div_data_valid_out),
        .error_out(div_error_out),
        .busy_out(div_busy_out)
    );

    
endmodule

`default_nettype wire

