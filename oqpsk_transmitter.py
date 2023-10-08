# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Oqpsk Transmitter
# Generated: Wed Aug  7 12:24:16 2019
##################################################


from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.filter import firdes


class oqpsk_transmitter(gr.hier_block2):

    def __init__(self, a=0.35, fc=1000, num_taps=11, samp_rate=32000, sps=200, sym_rate=160):
        gr.hier_block2.__init__(
            self, "Oqpsk Transmitter",
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
            gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.a = a
        self.fc = fc
        self.num_taps = num_taps
        self.samp_rate = samp_rate
        self.sps = sps
        self.sym_rate = sym_rate

        ##################################################
        # Blocks
        ##################################################
        self.root_raised_cosine_filter_0_0 = filter.fir_filter_fff(1, firdes.root_raised_cosine(
        	1, samp_rate, sym_rate, a, num_taps))
        self.root_raised_cosine_filter_0 = filter.fir_filter_fff(1, firdes.root_raised_cosine(
        	1, samp_rate, sym_rate, a, num_taps))
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_repeat_0_0 = blocks.repeat(gr.sizeof_float*1, int(samp_rate/sym_rate))
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, sps)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, int(sps/2))
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_imag_0 = blocks.complex_to_imag(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, fc, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, fc, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self, 0))
        self.connect((self.blocks_complex_to_imag_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_throttle_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_repeat_0_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_repeat_0_0, 0))
        self.connect((self.blocks_throttle_1, 0), (self.root_raised_cosine_filter_0_0, 0))
        self.connect((self, 0), (self.blocks_complex_to_imag_0, 0))
        self.connect((self, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.blocks_multiply_xx_0, 1))

    def get_a(self):
        return self.a

    def set_a(self, a):
        self.a = a
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.sym_rate, self.a, self.num_taps))
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.sym_rate, self.a, self.num_taps))

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.analog_sig_source_x_0_0.set_frequency(self.fc)
        self.analog_sig_source_x_0.set_frequency(self.fc)

    def get_num_taps(self):
        return self.num_taps

    def set_num_taps(self, num_taps):
        self.num_taps = num_taps
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.sym_rate, self.a, self.num_taps))
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.sym_rate, self.a, self.num_taps))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.sym_rate, self.a, self.num_taps))
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.sym_rate, self.a, self.num_taps))
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.blocks_repeat_0_0.set_interpolation(self.samp_rate/self.sym_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.blocks_repeat_0.set_interpolation(self.sps)
        self.blocks_delay_0.set_dly(self.sps/2)

    def get_sym_rate(self):
        return self.sym_rate

    def set_sym_rate(self, sym_rate):
        self.sym_rate = sym_rate
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.sym_rate, self.a, self.num_taps))
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.sym_rate, self.a, self.num_taps))
        self.blocks_repeat_0_0.set_interpolation(self.samp_rate/self.sym_rate)
