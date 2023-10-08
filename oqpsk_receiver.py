# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Oqpsk Receiver
# Generated: Wed Jul 31 18:45:47 2019
##################################################


from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window


class oqpsk_receiver(gr.hier_block2):

    def __init__(self, a=0.35, fc=1000, num_taps=11, samp_rate=32000, sym_rate=160):
        gr.hier_block2.__init__(
            self, "Oqpsk Receiver",
            gr.io_signature(1, 1, gr.sizeof_float*1),
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.a = a
        self.fc = fc
        self.num_taps = num_taps
        self.samp_rate = samp_rate
        self.sym_rate = sym_rate

        ##################################################
        # Blocks
        ##################################################
        self.root_raised_cosine_filter_0_1_0_0 = filter.fir_filter_fff(1, firdes.root_raised_cosine(
        	1, samp_rate, sym_rate, a, num_taps))
        self.root_raised_cosine_filter_0_1_0 = filter.fir_filter_fff(1, firdes.root_raised_cosine(
        	1, samp_rate, sym_rate, a, num_taps))
        self.hilbert_fc_0 = filter.hilbert_fc(65, firdes.WIN_HAMMING, 6.76)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_xx_0 = blocks.multiply_const_ff(-1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_real_1 = blocks.complex_to_real(1)
        self.blocks_complex_to_imag_1 = blocks.complex_to_imag(1)
        self.analog_sig_source_x_1_0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, -fc, 1, 0)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -fc, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.analog_sig_source_x_1_0, 0), (self.blocks_multiply_xx_1_0, 1))
        self.connect((self.blocks_complex_to_imag_1, 0), (self.blocks_multiply_const_xx_0, 0))
        self.connect((self.blocks_complex_to_real_1, 0), (self.root_raised_cosine_filter_0_1_0_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self, 0))
        self.connect((self.blocks_multiply_const_xx_0, 0), (self.root_raised_cosine_filter_0_1_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_complex_to_real_1, 0))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.blocks_complex_to_imag_1, 0))
        self.connect((self.hilbert_fc_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.hilbert_fc_0, 0), (self.blocks_multiply_xx_1_0, 0))
        self.connect((self, 0), (self.hilbert_fc_0, 0))
        self.connect((self.root_raised_cosine_filter_0_1_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.root_raised_cosine_filter_0_1_0_0, 0), (self.blocks_float_to_complex_0, 0))

    def get_a(self):
        return self.a

    def set_a(self, a):
        self.a = a
        self.root_raised_cosine_filter_0_1_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.sym_rate, self.a, self.num_taps))
        self.root_raised_cosine_filter_0_1_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.sym_rate, self.a, self.num_taps))

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.analog_sig_source_x_1_0.set_frequency(-self.fc)
        self.analog_sig_source_x_1.set_frequency(-self.fc)

    def get_num_taps(self):
        return self.num_taps

    def set_num_taps(self, num_taps):
        self.num_taps = num_taps
        self.root_raised_cosine_filter_0_1_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.sym_rate, self.a, self.num_taps))
        self.root_raised_cosine_filter_0_1_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.sym_rate, self.a, self.num_taps))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.root_raised_cosine_filter_0_1_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.sym_rate, self.a, self.num_taps))
        self.root_raised_cosine_filter_0_1_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.sym_rate, self.a, self.num_taps))
        self.analog_sig_source_x_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)

    def get_sym_rate(self):
        return self.sym_rate

    def set_sym_rate(self, sym_rate):
        self.sym_rate = sym_rate
        self.root_raised_cosine_filter_0_1_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.sym_rate, self.a, self.num_taps))
        self.root_raised_cosine_filter_0_1_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.sym_rate, self.a, self.num_taps))
